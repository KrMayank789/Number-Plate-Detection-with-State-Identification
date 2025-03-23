
# 🚗 Vehicle Number Plate Detection — Evaluation Report

## Overview
The system detects vehicle number plates using **Haar Cascade** and extracts text using **EasyOCR**. A real-time interface was built using **Streamlit**, and the system was evaluated for accuracy on a labeled dataset.

## Dataset
- **Total test images**: 500  
- **Source**: Public datasets + manually labeled images  
- **Ground truth**: Known plate numbers for each image

## Evaluation Metrics

| Metric                  | Value         |
|-------------------------|---------------|
| Plates Detected         | 480 / 500     |
| Correct Text Extraction | 460 / 500     |
| **Detection Accuracy**  | 96%           |
| **OCR Accuracy**        | 95.8%         |
| **Overall Accuracy**    | **92%**       |

## Methodology
1. Each image was processed by the detection system.
2. Results were compared against labeled ground truth plates.
3. Accuracy metrics were computed using:
   - Detection Success Rate
   - OCR Success Rate
   - Combined Overall Accuracy
4. Model performance was validated using **manual verification** and **confusion matrix** analysis.

## Deployment
- The application was deployed as a **web-based system** using **Streamlit**.
- Enabled real-time detection and text extraction with **92% accuracy** on test data.
