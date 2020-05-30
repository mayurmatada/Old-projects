from flask import Flask, render_template, request
import tensorflow as tf
import io
import base64
import numpy as np
import PIL

app = Flask(__name__)

global model
model = tf.keras.models.load_model('./model')

def processimage(rawimg):
    img = rawimg.split('base64, ')[1]
    img = base64.b64decode(img, altchars=[str])
    img = io.BytesIO(img)
    img = PIL.Image.open(img)
    img = img.convert('L')
    img.resize((28, 28), PIL.Image.ANTIALIAS)
    img = 1-np.array(img, np.float32)
    img = img/255
    img = img.reshape(1, 28, 28, 1)
    return img

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict/", methods=['GET', 'POST'])
def predict():
    img = processimage(request.get_data())
    prediction = model.predict_classes(img)
    return prediction

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)