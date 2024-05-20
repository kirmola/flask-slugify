from flask import Flask, request, jsonify
from slugify import slugify
from os import environ
from shortuuid import ShortUUID

app = Flask(__name__)

#################  Convert text into slug
@app.route('/text')
def slugify_text():
    """
    Endpoint to accept GET requests and slugify text.
    """
    text = request.args.get('text', '')  # Get text from query parameters
    slugified_text = slugify(text)
    return slugified_text, 200


#################   Convert quote to unique urls

@app.route('/quoteslug')
def quote_slugify():
    text = request.args.get('quote', '')
    random_postfix = ShortUUID().random(length=6)
    slugified_text = f"{slugify(text, word_boundary=True, max_length=25)}-{random_postfix}" 
    return slugified_text, 200




###############   Added images in list in excel ########
@app.route("/list-concat")
def concat_list_in_cell():
    text = request.args.get("quote", "")
    img1_suffix = ["1.png", "1-thumb.png"]
    final_image_urls = [f"{text}-{i}" for i in img1_suffix]
    return final_image_urls