from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

app = Flask(__name__)

generator = load_model('generator_model.h5')

@app.route('/')
def index():
    img_path = request.args.get('img_path')
    return render_template('index.html', img_path=img_path)

@app.route('/generate', methods=['POST'])
def generate():
    noise = np.random.normal(0, 1, (1, 100))
    generated_image = generator.predict(noise)
    generated_image = 0.5 * generated_image + 0.5  # Rescalingg

    img_path = 'static/generated_image.png'
    plt.imshow(generated_image[0, :, :, 0], cmap='gray')
    plt.axis('off')
    plt.savefig(img_path)
    plt.close()

    return redirect(url_for('index', img_path=img_path))

if __name__ == '__main__':
    app.run(debug=True)
