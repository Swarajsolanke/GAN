from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.models import load_model

import numpy as np
from PIL import Image
import io
import base64


app = Flask(__name__)


# Load the GAN model
model = load_model(r'C:\Users\rajpu\OneDrive\Desktop\FInal year project data\GAN\new.h5')
print(model)
SIZE = 256  # Ensure this matches your model's input size



from PIL import Image
import io
import numpy as np
import base64
from flask import Flask, render_template, request

app = Flask(__name__)

SIZE = 256  # Adjust SIZE as needed

# Function to process and resize the image
def process_image(image_data):
    image = Image.open(io.BytesIO(image_data)).convert('L')  # Convert image to grayscale (L mode)
    image = image.resize((SIZE, SIZE))
    image_array = np.array(image) / 255.0  # Normalize image to [0,1] range
    return image_array.reshape(1, SIZE, SIZE, 1)  # Keep only one channel (grayscale)

# Function to convert generated image array to base64
def array_to_base64(img_array):
    img = Image.fromarray((img_array * 255).astype('uint8'))
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

# Route to upload and display image
@app.route("/main", methods=["GET", "POST"])
def upload_and_predict():
    if request.method == "POST":
        # Get the uploaded file
        file = request.files["file"]
        if file:
            image_data = file.read()
            # Process the grayscale image and make prediction
            processed_image = process_image(image_data)
            predicted = np.clip(model.predict(processed_image), 0.0, 1.0).reshape(SIZE, SIZE, 3)  # Predict color image
            
            # Convert prediction to base64 to render on the webpage
            predicted_base64 = array_to_base64(predicted)

            return render_template("index.html", uploaded_image=base64.b64encode(image_data).decode('utf-8'),
                                   generated_image=predicted_base64)

    return render_template("index.html", uploaded_image=None, generated_image=None)


@app.route('/')
def index():
    return render_template('demo.html')


if __name__ == "__main__":
    app.run(debug=True)


