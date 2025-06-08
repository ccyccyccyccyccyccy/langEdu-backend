
#http://127.0.0.1:5000/

import flask
from flask import request, send_file, jsonify
import os
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

@app.route('/')
def hello():
   return 'Hello, Pythongeeks!'

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'backend/uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create folder if it doesn’t exist
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask!"})

#curl.exe -X POST -F "pdf=@vertopal.com_Lab5.pdf" http://127.0.0.1:5000/upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf' not in request.files:
        return 'No file part', 400
    
    file = request.files['pdf']

    if file.filename == '':
        return 'No selected file', 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)  # Save file properly
    return jsonify({"message": "File uploaded successfully"})

#curl.exe -X GET http://127.0.0.1:5000/download/vertopal.com_Lab5.pdf --output hello.pdf
@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)  # Assuming files are stored in 'uploads' folder
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit
