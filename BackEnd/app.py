
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from ultralytics import YOLO
import os
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__, static_folder="../", static_url_path="")
CORS(app)

# Define the uploads folder
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Load the best trained YOLOv8 model
model = YOLO('models/best.pt')

# Function to validate file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Serve the React app's index.html
@app.route('/')
def serve_react():
    return send_from_directory(app.static_folder, 'index1.html')

# Serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        try:
            results = model(file_path)
            result_data = []

            for r in results:
                for box in r.boxes.data.tolist():
                    x1, y1, x2, y2, score, class_id = box
                    result_data.append({
                        'class': model.names[int(class_id)],
                        'confidence': round(score * 100, 2)  # convert to percentage
                    })

            if result_data:
                diagnosis = result_data[0]['class']
                confidence = result_data[0]['confidence']
            else:
                diagnosis = "non-cancer"
                confidence = 0.0

            return jsonify({
                'success': True,
                'filename': filename,
                'image_url': f"/uploads/{filename}",
                'results': {
                    'ptb_result': {
                        'diagnosis': diagnosis,
                        'confidence': confidence,
                        'class': diagnosis,
                        'image_url': f"/uploads/{filename}"
                    }
                }
            })
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)}), 500

    else:
        return jsonify({'success': False, 'error': 'Invalid file type'}), 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
#---------------------------------------------------------
