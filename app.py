from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('file_iris.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html', predict='')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])  # Fixed typo
        petal_width = float(request.form['petal_width'])
        pred = model.predict(np.array([[sepal_length, sepal_width, petal_length, petal_width]]))
        return render_template('index.html', predict=pred[0])
    except ValueError:
        return render_template('index.html', predict="Invalid input: Please enter numeric values")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)