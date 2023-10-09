import base64

from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__, static_url_path='/static')

# Load the trained model
model_path = "C:\\Users\\imb\\PycharmProjects\\Binary-classifier\\saved_models\\Binary_classifier.h5"
model = load_model(model_path)

# Define class names
class_names = ['Pizza', 'Steak']

# Function to preprocess an uploaded image
def load_and_prep_image(filename, img_shape=224):
    img = tf.io.read_file(filename)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.resize(img, size=[img_shape, img_shape])
    img = img / 255.0
    return img

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle image upload from the form
        file = request.files["file"]
        if file:
            # Save the uploaded image temporarily
            temp_image_path = "temp_image.jpg"
            file.save(temp_image_path)

            # Preprocess the image and make a prediction
            img = load_and_prep_image(temp_image_path)
            pred = model.predict(tf.expand_dims(img, axis=0))
            pred_class = class_names[int(tf.round(pred)[0][0])]

            # Remove the temporary image file
            #os.remove(temp_image_path)

            encoded_image = base64.b64encode(img.numpy()).decode("utf-8")


            prediction = {
                "predicted_class": pred_class,
                "image_path": f"data:image/jpeg;base64,{encoded_image}"  # Include the base64-encoded image in the response
            }

            # Render the result on the web page
            return render_template("index.html", prediction=prediction)

    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
