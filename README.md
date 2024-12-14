# Vehicle Number Plate Detection and State Identification 🚗🚘

## Overview  
This project simplifies vehicle identification by automatically detecting number plates, extracting text using OCR, and identifying the state of registration. It combines powerful tools like Haar Cascade and EasyOCR with a user-friendly Streamlit interface to deliver a smooth, real-time experience.  

---

## Features  
- **Real-Time Detection**: Quickly detects number plates in videos or images.  
- **Text Recognition**: Extracts plate text accurately with EasyOCR.  
- **State Identification**: Maps the text to state codes to identify the origin of the vehicle.  
- **Interactive GUI**: A simple and clean Streamlit app makes it easy to upload files and view results.  
- **Extensible Design**: Can grow to support additional features like multilingual OCR or centralized vehicle databases.  

---

## Technology Stack  
- **Language**: Python  
- **Libraries**: OpenCV, EasyOCR, Streamlit  
- **Detection Method**: Haar Cascade Classifier  

---

## How It Works  
1. **Video or Image Input**: The system captures frames from videos or processes uploaded images.  
2. **Plate Detection**: Number plates are identified using Haar Cascade.  
3. **Text Extraction**: EasyOCR extracts text from the detected plates.  
4. **State Mapping**: Extracted text is matched with predefined state codes.  
5. **Output**: Displays the number plate, recognized text, and the state name in the GUI.  

---

## Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/KrMayank789/Number-Plate-Detection-with-State-Identification.git
   
2. Navigate to the project directory:
    ```bash
    cd vehicle-number-plate-detection

3. Install the required libraries:
   ```bash
    pip install -r requirements.txt

4. Run the app:
    ```bash
    streamlit run app.py

5. Upload a video or image in the app.
6. View the detected number plate, extracted text, and the identified state directly in the interface.

## Output:

 ![Screenshot 2024-12-06 072800](https://github.com/user-attachments/assets/d268d446-b853-4974-9c50-752d59c64570)



## And that's it have a smooth ride ahead! 🚗

---

&copy; KrMayank789


