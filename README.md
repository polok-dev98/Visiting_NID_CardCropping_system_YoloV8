# Visiting and NID Card Cropping System using YOLOv8

This project is a web application designed to detect and crop visiting and NID cards from uploaded images using a YOLOv8 model. The application uses Flask as the web framework, OpenCV for image processing, and the Ultralytics YOLO model for object detection.

## Project Structure
├── model
│ └── seg.pt
├── static
│ ├── background.jpg
│ └── company_logo.png
├── templates
│ └── index.html
├── app.py
└── requirements.txt


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
    ![Screenshot 2024-06-12 142440](https://github.com/polok-dev98/Visiting_NID_CardCropping_system_YoloV8/assets/104290708/9cc3f568-3eef-4088-8695-b99e63af739a)

   </br>
   </br>

   ![Screenshot 2024-06-12 142345](https://github.com/polok-dev98/Visiting_NID_CardCropping_system_YoloV8/assets/104290708/9628828d-2962-4829-acef-adec57f5b24a)

   </br>

    



## Example

1. Navigate to the homepage.

2. Upload an image containing a card.

3. The application will process the image and return the cropped card if detected.

4. You can view and download the cropped image.



## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Ultralytics](https://ultralytics.com/) for the YOLOv8 model.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [OpenCV](https://opencv.org/) for image processing.

