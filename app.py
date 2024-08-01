from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Define your Hugging Face Gradio Space API URL
HF_API_URL = 'https://huggingface.co/spaces/Sakibrumu/Food_Image_Classification/api/predict/'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    files = {'file': (file.filename, file.read(), file.content_type)}

    try:
        response = requests.post(HF_API_URL, files=files)
        response.raise_for_status()
        result = response.json()
        return jsonify(result)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
