from flask import Flask, render_template, request
from app import deep
from werkzeug.utils import secure_filename
import os

application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = './img'

@application.route("/")
def index():
    return render_template('index.html')

@application.route('/predict', methods=['POST'])
def predict():
    f = request.files['file']
    filename = str(secure_filename(f.filename))
    basedir = os.path.abspath(os.path.dirname(__file__))
    f.save(str(os.path.join(application.config['UPLOAD_FOLDER'])+"/"+filename))
    result = deep(f'./img/{filename}')
    confidence = round(result['confidence'] * 100,2)
    os.remove(str(os.path.join(application.config['UPLOAD_FOLDER'])+"/"+filename))
    return render_template('result.html', result=f"{result['class']}, {confidence}%")

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=True)
