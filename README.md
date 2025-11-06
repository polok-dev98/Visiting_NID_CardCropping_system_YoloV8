

<img width="1843" height="914" alt="Screenshot from 2025-11-06 20-53-53" src="https://github.com/user-attachments/assets/3bde360f-556c-43d9-b392-d1d8f89642a9" />



# Visiting and NID Card Cropping System using YOLOv8 🎯

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3%2B-lightgrey)](https://flask.palletsprojects.com/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Object--Detection-orange)](https://docs.ultralytics.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Image--Processing-brightgreen)](https://opencv.org/)

## 🚀 Project Overview

This project is an intelligent web application that automatically detects and crops visiting cards and National ID (NID) cards from uploaded images using a fine-tuned YOLOv8 model. The system provides accurate document extraction with a user-friendly web interface, making it ideal for digitization and document processing workflows.

<div align="center">


</div>

## 🏗️ Project Structure

```
card-cropping-system/
│
├── 🐍 app.py                      # Main Flask application
├── 📋 requirements.txt            # Python dependencies
├── 📚 README.md                   # Project documentation
├── 📄 LICENSE                     # MIT License
├── 📄 Dockerfile                   
│
├── 🤖 model/
│   └── seg.pt                     # Fine-tuned YOLOv8 model weights
│
├── 🎨 static/
│   ├── style.css                  # Web interface styling                
│   └── logo.png                   # Company logo
│
├── 📄 templates/
│   └── index.html                 # Main web interface template
                 
```


- `model/seg.pt`: The Fine-tuned YOLOV8 model file.
- `static/`: Contains background image and company logo.
- `templates/`: Contains the HTML template for the web application.
- `app.py`: The main Flask application.
- `requirements.txt`: Lists the Python dependencies.
- `Dockerfile`: For deployment.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or newer
- pip package manager
- Git for version control

### 1. Clone the Repository
```bash
git clone https://github.com/polok-dev98/Visiting_NID_CardCropping_system_YoloV8.git
cd Visiting_NID_CardCropping_system_YoloV8
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch Web Application
```bash
python app.py
```
Visit **http://localhost:5000** to access the card cropping interface.

---

## 🔧 Technical Implementation

### Model Architecture
```python
# YOLOv8 Model Loading
model = YOLO('model/seg.pt')

# Detection Configuration
conf_threshold = 0.5  # Minimum confidence for detection
```

### Image Processing Pipeline
1. **Image Upload**: User uploads image through web interface
2. **Format Validation**: Check for supported image formats
3. **YOLO Inference**: Run object detection on uploaded image
4. **Confidence Filtering**: Filter detections above threshold
5. **Bounding Box Extraction**: Calculate precise crop coordinates
6. **Image Cropping**: Extract card regions using OpenCV
7. **Result Saving**: Save cropped images to output directory
8. **Response Generation**: Display results to user

### Web Application Flow
```
User Upload → Flask API → YOLO Detection → OpenCV Cropping → Result Display
```

### Key Functions:
- **`/`**: Serve main web interface
- **`/upload`**: Handle image upload and processing
- **`/outputs/<filename>`**: Serve processed images

---

## 🎯 Usage Examples

### Web Interface Workflow

1. **Access Homepage**
</br> 
<img width="1843" height="914" alt="Screenshot from 2025-11-06 20-59-15" src="https://github.com/user-attachments/assets/0dc91c8a-53a4-4580-b4cf-5ceb0ac3d835" />


</br>
</br>

3. **Upload Image**: Drag and drop or click to upload image containing cards
4. **Automatic Processing**: System detects and crops cards automatically
5. **View Results**: See cropped cards with download options

### Successful Detection Examples

**Visiting Card Detection:**
</br>
</br>
<img width="1843" height="914" alt="Screenshot from 2025-11-06 21-16-39" src="https://github.com/user-attachments/assets/e1c4b7cd-184d-4949-ab0c-bf774553d826" />

</br>
</br>

<img width="1843" height="914" alt="Screenshot from 2025-11-06 21-19-02" src="https://github.com/user-attachments/assets/d565a40e-8737-447a-bb53-1dc5f9881156" />

</br>
</br>

**NID Card Detection:**
</br>
</br>
<img width="1843" height="914" alt="Screenshot from 2025-11-06 21-00-23" src="https://github.com/user-attachments/assets/0e189e40-7dfe-4ce9-aae6-965307426d7d" />

</br>
</br>

<img width="1843" height="914" alt="Screenshot from 2025-11-06 21-05-11" src="https://github.com/user-attachments/assets/a051e57a-1360-40b4-ac77-b7ae3b3802a9" />
</br>


</br>

---

## 📊 Performance Metrics

### Detection Accuracy
- **Model**: YOLOv8 Fine-tuned on custom dataset
- **Classes**: Visiting Card, NID Card
- **Confidence Threshold**: 0.5 (configurable)
- **Processing Speed**: Real-time inference on standard hardware

### Image Processing
- **Format Support**: Multiple image formats
- **Size Handling**: Automatic resizing and optimization
- **Quality Preservation**: Maintains original image quality during cropping

---

## 🌐 Live Demo

Experience the system live on Hugging Face Spaces:
### [🚀 Live Demo on Hugging Face](https://huggingface.co/spaces/iluasdfiuasfd/Visiting-and-NID-Card-Cropping)

---

## 🔍 How It Works

### 1. **Object Detection Pipeline**
```
Input Image → YOLOv8 Inference → Bounding Box Prediction → Confidence Filtering → Card Extraction
```

### 2. **Web Application Architecture**
```
Frontend (HTML/JS/CSS)
        ↓
    Flask API (Python)
        ↓
  YOLOv8 Model
        ↓
  OpenCV Processing
        ↓
Cropped Images + Display
```

### 3. **Technical Stack**
```
User Interface: HTML5 + CSS3 + JavaScript
Backend Framework: Flask
AI Model: YOLOv8 (Ultralytics)
Image Processing: OpenCV
File Handling: Python OS module
```

---


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.
---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developed by

**Asif Pervez Polok** 💻

[![Email](https://img.shields.io/badge/Email-asifperveznstu.jsr369@gmail.com-blue?style=flat-square&logo=gmail)](mailto:asifperveznstu.jsr369@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-polok98-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/polok98/)
[![GitHub](https://img.shields.io/badge/GitHub-polok--dev98-black?style=flat-square&logo=github)](https://github.com/polok-dev98)

**"Simplifying document digitization through AI-powered automation"** 🚀

---

## 🔗 References & Acknowledgments

- [Ultralytics YOLOv8](https://docs.ultralytics.com/) - State-of-the-art object detection
- [Flask Web Framework](https://flask.palletsprojects.com/) - Lightweight Python web framework
- [OpenCV](https://opencv.org/) - Computer vision and image processing
- [Hugging Face Spaces](https://huggingface.co/spaces) - Platform for demo deployment

---

<div align="center">

### ⭐ **Star this repo if you find it helpful!** ⭐

*Your support helps improve document processing automation!*

</div>

---
