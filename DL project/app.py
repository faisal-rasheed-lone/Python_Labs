from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import cv2  # OpenCV for image processing

# Define the custom loss function
def dice_loss_plus_1focal_loss(y_true, y_pred):
    # Define your custom loss logic here
    # For example, you can combine dice loss and focal loss
    # Replace this with your actual loss function implementation
    # ...

# Load your saved model while specifying the custom_objects parameter
model = tf.keras.models.load_model('model.h5', custom_objects={'dice_loss_plus_1focal_loss': dice_loss_plus_1focal_loss})


app = Flask(__name__)

# Load your saved model
model = load_model('model.h5')

# Define a function to preprocess the input image
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))  # Adjust target size as needed
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return img

@app.route('/')
def index():
    return render_template('index.html')  # Create an HTML form for uploading images

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        img_path = 'temp.jpg'  # Save the uploaded image temporarily
        file.save(img_path)

        # Preprocess the image
        img = preprocess_image(img_path)

        # Make predictions
        prediction = model.predict(img)

        # Process the prediction result
        # In this example, we assume prediction is an image (semantic segmentation)
        # Convert the image from a NumPy array to a format suitable for sending as JSON
        prediction_image = prediction[0].astype(np.uint8)  # Adjust data type as needed

        # You can also return other relevant information along with the segmented image
        result = {
            'segmented_image': prediction_image.tolist(),
            'class_label': 'Class 1',  # Replace with your prediction
            'confidence': float(np.max(prediction))  # Replace with confidence score
        }

        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
