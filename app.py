from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Interview Bot!"

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    upload_folder = 'uploads'
    os.makedirs(upload_folder, exist_ok=True)
    try:
        file = request.files['file']
        if file:
            file.save(os.path.join(upload_folder, file.filename))
            return jsonify({'message': 'PDF uploaded successfully!'})
        else:
            return jsonify({'message': 'No file provided'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
