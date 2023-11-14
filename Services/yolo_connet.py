from ultralytics import YOLO
import cv2
import torch


model = YOLO("./ML_AI_NN/best.pt")
class_colors = \
    {
        0: (255, 0, 0),
        1: (0, 255, 0),
        2: (0, 0, 255),
        3: (255, 255, 0)
    }

class_font = cv2.FONT_HERSHEY_SIMPLEX
class_font_scale = 1.2