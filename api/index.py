from flask import Flask, request, jsonify
from slugify import slugify
from os import environ

app = Flask(__name__)

@app.route('/')
def slugify_text():
    """
    Endpoint to accept GET requests and slugify text.
    """
    text = request.args.get('text', '')  # Get text from query parameters
    slugified_text = slugify(text)
    return jsonify({'slugified_text': slugified_text}), 200
