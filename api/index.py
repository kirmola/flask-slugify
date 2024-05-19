from flask import Flask, request, jsonify
from slugify import slugify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def slugify_text():
    """
    Endpoint to accept POST requests and slugify text.
    """
    if request.method == 'POST':
        text = request.form.get('text', '')  # Get text from form data
        slugified_text = slugify(text)
        return jsonify({'slugified_text': slugified_text}), 200