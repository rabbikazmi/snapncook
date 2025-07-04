# backend/main.py

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
from PIL import Image
import numpy as np
import io

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace * with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your trained model
model = YOLO("best.pt")

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read and convert the uploaded image
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    img_array = np.array(img)

    # Perform prediction
    results = model(img_array)
    result_img = results[0].plot()  # Plot bounding boxes
    result_pil = Image.fromarray(result_img)

    # Convert result image to bytes
    buf = io.BytesIO()
    result_pil.save(buf, format='JPEG')
    byte_im = buf.getvalue()

    # Return hex-encoded image for frontend display
    return {"image": byte_im.hex()}
