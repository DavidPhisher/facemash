from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Example dataset of images
images = [
    ["img1", "static/images/1.jpg", 0],
    ["img2", "static/images/2.jpg", 0],
    ["img2", "static/images/3.jpg", 0],
    ["img2", "static/images/4.jpg", 0],
    ["img2", "static/images/5.jpg", 0],
    ["img2", "static/images/6.jpg", 0],
    ["img2", "static/images/7.jpg", 0],
    ["img2", "static/images/8.jpg", 0],
    ["img2", "static/images/9.jpg", 0],
    ["img2", "static/images/10.jpg", 0]
    # Add more images as needed
]


@app.route('/')
def index():
    return render_template('index.html', images=images)


@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()
    winner_id = data['winner_id']

    # Update vote count logic (here, just incrementing for the winner)
    for image in images:
        if image[0] == winner_id:
            image[2] += 1

    # Return updated image data
    return jsonify(images=images)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
