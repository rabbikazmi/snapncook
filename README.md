<h1 align="center">🍳 snapncook</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi" />
  <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-orange?logo=opencv" />
  <img src="https://img.shields.io/badge/YOLOv11-Custom--Build-red?logo=ai" />
  <img src="https://img.shields.io/badge/Gemini-Enabled-yellow?logo=google" />
</p>

snapncook is an AI-powered web application that helps you cook smarter and reduce food waste. Just snap a photo of your fridge or kitchen items — our custom-trained YOLOv11 model detects ingredients, and we suggest recipes based on what’s available. Optionally, Gemini API integration helps enhance recipe suggestions or interactions.


##  Features

-  Ingredient detection using **YOLOv11**
-  FastAPI-powered backend
-  Recipe suggestion system (Gemini-enhanced)
-  Static frontend with HTML/CSS/JS
-  Gemini API integration via `.env`
-  Future-ready for voice, grocery suggestions, and more!

##  Tech Stack

| Layer     | Technology              |
|-----------|--------------------------|
| Model     | YOLOv11 (Ultralytics `best.pt`) |
| Backend   | Python, FastAPI          |
| Frontend  | HTML, CSS, JavaScript    |
| API       | Gemini (Google)          |

##  Project Structure
```
snapncook/
│
├── app/
│   ├── main.py                # FastAPI backend entry point
│   ├── model_loader.py        # Loads YOLOv8 model
│   ├── image_processor.py     # Image handling logic
│   ├── best.pt                # Trained YOLOv8 model
│   └── .env                   # Environment variables (ignored in Git)
│
├── static/
│   └── css/style.css          # UI styles
│   └── script.js              # Frontend JS logic
│
├── templates/
│   └── index.html             # Main HTML page
│
├── model results/             # Output images from detection
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

```


## Getting Started (Local Development)

1. Clone the Repository
```
git clone https://github.com/yourusername/snapncook.git
cd snapncook/app
```
2. Install Python Dependencies
```
pip install -r ../requirements.txt
```
3. Add .env File
```
GEMINI_API_KEY=your-gemini-api-key-here
```
4. Run the FastAPI Server
```
uvicorn main:app --reload
```
## YOLOv11 Notes

This project uses the latest YOLOv8 via the Ultralytics package, sometimes referred to as YOLOv11 due to its community-enhanced capabilities.

## Future Enhancements
- Voice-based ingredient input
- Grocery list generator
- Save and share favorite recipes
- Nutrition breakdowns
- More advanced recipe AI using Gemini Pro Vision

## Contributing

PRs and feedback are always welcome!
Fork the repo, create a feature branch, and submit a pull request.

---

