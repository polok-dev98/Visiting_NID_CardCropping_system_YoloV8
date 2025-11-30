from flask import Flask, request, jsonify, render_template, send_from_directory
import cv2
from ultralytics import YOLO
import os
import time
import torch

app = Flask(__name__)

# Initialize YOLO model
try:
    inst_model = YOLO('model/seg.pt')
    print("YOLO model loaded successfully with ultralytics==8.2.42")
except Exception as e:
    print(f"Error loading YOLO model: {e}")
    inst_model = None

# Function to perform YOLO prediction and crop detected card images
def detect_and_crop(image_path, output_folder):
    if inst_model is None:
        return None
        
    # Read the image
    frame = cv2.imread(image_path)
    if frame is None:
        print("Error: Could not read image")
        return None

    try:
        # Perform YOLO prediction
        instance_results = inst_model.predict(frame)
        result = instance_results[0]

        if result.boxes and len(result.boxes) > 0:
            # Loop through detected boxes
            for box in result.boxes:
                class_id = int(box.cls[0].item())
                conf = box.conf[0].item()

                # Check if the detected object is a card with high confidence
                if class_id == 0 and conf >= 0.70:
                    # Crop the detected card
                    x1, y1, x2, y2 = box.xyxy[0]
                    cropped_card = frame[int(y1):int(y2), int(x1):int(x2)]

                    # Save the cropped card to the output folder
                    output_filename = os.path.join(output_folder, "cropped_card.jpg")
                    if os.path.exists(output_filename):
                        os.remove(output_filename)
                    cv2.imwrite(output_filename, cropped_card)
                    return output_filename
        return None
    except Exception as e:
        print(f"Error during detection: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect-and-crop', methods=['POST'])
def detect_and_crop_endpoint():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Validate file type
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}
    if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return jsonify({'error': 'Invalid file type. Please upload an image.'}), 400

    # Create the output folder if it doesn't exist
    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        # Clear previous images in the output folder
        try:
            files_in_output_folder = os.listdir(output_folder)
            for file_in_folder in files_in_folder:
                file_path = os.path.join(output_folder, file_in_folder)
                if os.path.isfile(file_path):
                    os.remove(file_path)
        except Exception as e:
            print(f"Error clearing output folder: {e}")

    # Save the uploaded file to a temporary location
    input_image_path = os.path.join(output_folder, file.filename)
    try:
        file.save(input_image_path)
    except Exception as e:
        return jsonify({'error': f'Error saving file: {str(e)}'}), 500

    start = time.time()

    # Call the function to detect and crop card images
    output_filename = detect_and_crop(input_image_path, output_folder)

    end = time.time()
    processing_time = round(end - start, 2)

    # Clean up input file
    try:
        if os.path.exists(input_image_path):
            os.remove(input_image_path)
    except Exception as e:
        print(f"Error cleaning up input file: {e}")

    if output_filename:
        return jsonify({
            'message': 'Card detected and cropped successfully!',
            'output_filename': "cropped_card.jpg",
            'processing_time': f"{processing_time} seconds"
        }), 200
    else:
        return jsonify({'message': 'No cards detected in the image with sufficient confidence'}), 200

@app.route('/output/<filename>')
def send_output_file(filename):
    try:
        return send_from_directory('output', filename)
    except Exception as e:
        return jsonify({'error': f'File not found: {str(e)}'}), 404

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'model_loaded': inst_model is not None,
        'versions': {
            'ultralytics': '8.2.42',
            'opencv': '4.10.0.84'
        }
    })

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=7860)