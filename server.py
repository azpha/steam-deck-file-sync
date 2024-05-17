from flask import Flask, flash, request
from werkzeug.utils import secure_filename
import os

port = 9999

# create dir if not existant
file_path = os.path.join(
    os.getcwd(),
    "files"
)
if not os.path.exists(file_path):
    os.mkdir(file_path)

# start + run flask app
app = Flask(__name__)
@app.route('/upload', methods=["POST"])
def upload():
    if 'file' not in request.files:
        flash("No file part")

    file = request.files["file"]
    if file.filename == '':
        flash("No selected file")

    filename = secure_filename(file.filename)
    file.save(os.path.join(file_path, filename))

    return "Uploaded!"

if __name__ == "__main__":
    app.run(debug=False,port=port,host="0.0.0.0")