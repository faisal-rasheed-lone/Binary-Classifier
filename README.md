
---

# Image Classifier Web Application

This web application allows users to upload an image, and it uses a deep learning model to predict whether the image contains pizza or steak.

![image](https://github.com/faisal-rasheed-lone/Binary-Classifier-ETE/assets/120707721/b8fbb206-6c25-4bac-99b3-40c29c5a5e05)


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/image-classifier-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd image-classifier-app
   ```

3. Create a Python virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the Flask application:

   ```bash
   python app.py
   ```

The web application should now be running locally at http://127.0.0.1:5000/.

## Usage

1. Access the web application by opening a web browser and navigating to http://127.0.0.1:5000/.

2. Click the "Choose File" button to select an image for classification. The image should be either a pizza or steak.

3. Click the "Upload and Predict" button to initiate the classification.

4. The application will display the predicted class (Pizza or Steak) and show the uploaded image along with the prediction.

## Features

- Image classification using a pre-trained deep learning model.
- User-friendly web interface for uploading images and viewing predictions.
- Display of predicted class and confidence score.

## Technologies Used

- Python
- Flask
- TensorFlow and Keras
- HTML/CSS for the web interface

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them to your branch.
4. Submit a pull request to the main repository.


---

Feel free to customize the README file further to include specific details about your project, usage instructions, or any additional information you want to provide to users and contributors.
