from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('decision_tree_diabetes.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        age = float(request.form['age'])
        bmi = float(request.form['bmi'])
        bp = float(request.form['bp'])
        s5 = float(request.form['s5'])
        s1 = float(request.form['s1'])

        features = np.array([[age, bmi, bp, s5, s1]])
        prediction = model.predict(features)[0]
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
