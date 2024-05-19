from flask import Flask, request, jsonify
from slugify import slugify
from os import environ

app = Flask(__name__)

@app.route('/', methods=['POST'])
def slugify_text():
    """
    Endpoint to accept POST requests and slugify text.
    """
    if request.method == 'POST':
        body = request.json  # Get text from form data
        text = body["text"]
        slugified_text = slugify(text)
        return jsonify({'slugified_text': slugified_text}), 200