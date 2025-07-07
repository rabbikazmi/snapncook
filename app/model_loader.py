from ultralytics import YOLO
from typing import Dict
import os


def load_models() -> Dict[str, YOLO]:
    """
    Load the YOLO model from disk and return in a dictionary.

    Returns:
        dict[str, YOLO]: Dictionary of models keyed by type ("s")
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "best.pt")
    models = {"s": YOLO(model_path)}
    return models