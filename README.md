# Visiting and NID Card Cropping System using YOLOv8

This project is a web application designed to detect and crop visiting and NID cards from uploaded images using a YOLOv8 model. The application uses Flask as the web framework, OpenCV for image processing, and the Ultralytics YOLO model for object detection. Here Fine-tuned the YOLOV8 model with real Cards and NIDs image, then use the trained model for detect and crop the card and NID.

![image](https://github.com/polok-dev98/Visiting_NID_CardCropping_system_YoloV8/assets/104290708/bfce35c9-963a-4bfc-93a8-62961885f4e8)



- `model/seg.pt`: The YOLO model file.
- `static/`: Contains background image and company logo.
- `templates/`: Contains the HTML template for the web application.
- `app.py`: The main Flask application.
- `requirements.txt`: Lists the Python dependencies.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

```sh
git clone (https://github.com/polok-dev98/Visiting_NID_CardCropping_system_YoloV8.git)
cd project_folder
```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask application:**

    ```sh
    python app.py
    ```

2. Open your web browser and go to [http://localhost:5000](http://localhost:5000).

3. Upload an image containing visiting or NID cards.

4. The application will detect and crop the cards, displaying the cropped images.

## How It Works

1. **Image Upload**: Users upload an image through the web interface.
2. **YOLO Prediction**: The application reads the image and uses the YOLOv8 model to detect cards.
3. **Card Cropping**: If a card is detected with high confidence, the application crops the card from the image.
4. **Result Display**: The cropped card image is saved and displayed to the user.

    



## Example

1. Navigate to the homepage.

2. Upload an image containing a card.

3. The application will process the image and return the cropped card if detected.

4. You can view and download the cropped image.  </br>


<img src="https://github.com/polok-dev98/Visiting_NID_CardCropping_system_YoloV8/assets/104290708/ab3a582e-9dc6-4688-8d31-c5a4038d0d5a" alt="image" width="400">

</br>
</br>

<img src="https://github.com/polok-dev98/Visiting_NID_CardCropping_system_YoloV8/assets/104290708/9628828d-2962-4829-acef-adec57f5b24a" alt="Screenshot" width="400">

</br>




## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Ultralytics](https://ultralytics.com/) for the YOLOv8 model.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [OpenCV](https://opencv.org/) for image processing.

