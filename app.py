from flask import Flask, request, jsonify, render_template, send_from_directory
import cv2
from ultralytics import YOLO
import os
import time

app = Flask(__name__)

# Initialize YOLO model
inst_model = YOLO('model/seg.pt')

# Function to perform YOLO prediction and crop detected card images
def detect_and_crop(image_path, output_folder):
    # Read the image
    frame = cv2.imread(image_path)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect-and-crop', methods=['POST'])
def detect_and_crop_endpoint():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']

    # Create the output folder if it doesn't exist
    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        # Clear previous images in the output folder
        files_in_output_folder = os.listdir(output_folder)
        for file_in_folder in files_in_output_folder:
            file_path = os.path.join(output_folder, file_in_folder)
            os.remove(file_path)

    # Save the uploaded file to a temporary location
    input_image_path = os.path.join(output_folder, file.filename)
    file.save(input_image_path)

    start = time.time()

    # Call the function to detect and crop card images
    output_filename = detect_and_crop(input_image_path, output_folder)

    end = time.time()
    processing_time = end - start

    if output_filename:
        return jsonify({
            'message': 'Cropped image saved successfully',
            'output_filename': "cropped_card.jpg",
            'processing_time': processing_time
        }), 200
    else:
        return jsonify({'message': 'No cards detected in the image'}), 200

@app.route('/output/<filename>')
def send_output_file(filename):
    return send_from_directory('output', filename)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
