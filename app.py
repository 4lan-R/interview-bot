from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Interview Bot!"


@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    file = request.files['file'] 
    file.save(os.path.join('uploads', file.filename))
    return jsonify({'message': 'PDF uploaded successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
