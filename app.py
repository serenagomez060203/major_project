from flask import Flask, render_template, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the pre-trained model
model = load_model('learning_style_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data['name']
    answers = data['answers']
    
    # Predict learning style
    prediction = model.predict(np.array([answers]))
    learning_style = np.argmax(prediction)  # Get the predicted class
    
    # Map prediction to learning style
    styles = ['Visual', 'Auditory', 'Kinesthetic']
    result = styles[learning_style]
    
    return jsonify({"name": name, "result": result})

@app.route('/result')
def result():
    name = request.args.get('name')
    result = request.args.get('result')
    return render_template('result.html', name=name, result=result)

if __name__ == '__main__':
    app.run(debug=True)