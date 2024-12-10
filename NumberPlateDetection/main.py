import cv2
import easyocr
import streamlit as st
import tempfile
import os

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'], gpu=False)

# Haar Cascade for license plate detection
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")

# State code dictionary

state_codes = {
    "Andhra Pradesh": "AP",
    "Arunachal Pradesh": "AR",
    "Assam": "AS",
    "Bihar": "BR",
    "Chhattisgarh": "CG",
    "Goa": "GA",
    "Gujarat": "GJ",
    "Haryana": "HR",
    "Himachal Pradesh": "HP",
    "Jharkhand": "JH",
    "Karnataka": "KA",
    "Kerala": "KL",
    "Madhya Pradesh": "MP",
    "Maharashtra": "MH",
    "Manipur": "MN",
    "Meghalaya": "ML",
    "Mizoram": "MZ",
    "Nagaland": "NL",
    "Odisha": "OD",
    "Punjab": "PB",
    "Rajasthan": "RJ",
    "Sikkim": "SK",
    "Tamil Nadu": "TN",
    "Telangana": "TS",
    "Tripura": "TR",
    "Uttar Pradesh": "UP",
    "Uttarakhand": "UK",
    "West Bengal": "WB",
    "Andaman and Nicobar Islands": "AN",
    "Chandigarh": "CH",
    "Dadra and Nagar Haveli": "DN",
    "Daman and Diu": "DD",
    "Delhi": "DL",
    "Jammu and Kashmir": "JK",
    "Ladakh": "LA",
    "Lakshadweep": "LD",
    "Puducherry": "PY"
}




def detect_plates(frame):
    """
    Detect license plates in a frame using Haar Cascade.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return plates


def extract_text_from_plate(plate_img):
    """
    Extract text from a cropped plate image using EasyOCR.
    """
    plate_text_list = reader.readtext(plate_img, detail=0)
    plate_text = "".join(plate_text_list).strip()
    return plate_text


def map_state_from_text(plate_text):
    """
    Map the extracted text to a state using the state code dictionary.
    """
    for state, code in state_codes.items():
        if plate_text.startswith(code):
            return state
    return "Unknown"


