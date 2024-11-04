from flask import Flask, render_template, request, jsonify
import os
import random

app = Flask(__name__)

# Path to the images directory
images_dir = 'static/images/'
# List of images
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
# Initialize votes for images
votes = {img: 0 for img in image_files}

@app.route('/')
def index():
    # Select two random images
    selected_images = random.sample(image_files, 2)
    return render_template('index.html', images=selected_images)

@app.route('/vote', methods=['POST'])
def vote():
    voted_image = request.json.get('image')
    if voted_image in votes:
        votes[voted_image] += 1
    return jsonify(votes=votes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
