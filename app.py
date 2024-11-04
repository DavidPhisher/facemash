from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Sample images and initial votes
images = [
    {"url": "static/image1.jpg", "votes": 0},
    {"url": "static/image2.jpg", "votes": 0},
]

@app.route('/')
def index():
    return render_template('index.html', images=images)

@app.route('/vote', methods=['POST'])
def vote():
    voted_image = request.json.get('image')
    for img in images:
        if img['url'] == voted_image:
            img['votes'] += 1
            break
    return jsonify(images=images)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
