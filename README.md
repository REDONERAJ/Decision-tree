# 🌳 Decision Tree Diabetes Progression Predictor

## 📌 About
**Decision Tree Regression** is a non-linear model that predicts a target variable by splitting the dataset into branches based on feature values. It uses if-else rules to form a tree structure, where each leaf node represents a predicted value, making it easy to interpret and visualize.

---

## 📂 Project Structure
```
├── model.py        # Trains the Decision Tree model on the Diabetes dataset
├── app.py          # Flask app to serve predictions
├── templates/
│   └── index.html  # Interactive UI for user input
├── decision_tree_diabetes.pkl  # Saved model file
└── requirements.txt # Project dependencies
```

---

## 📊 Dataset
We use the **Diabetes dataset** from `sklearn.datasets`, which contains medical details to predict disease progression.  
Features used:
- **Age** (years)
- **BMI** (kg/m²)
- **Blood Pressure** (mm Hg)
- **S5 Serum Measurement** (lab test)
- **S1 Serum Measurement** (lab test)

Target: A quantitative measure of diabetes progression one year after baseline.

---

## 🚀 How to Run
1. Clone this repository  
2. Install dependencies  
```
pip install -r requirements.txt
```
3. Train the model (optional, already trained in repo)  
```
python model.py
```
4. Run the Flask app  
```
python app.py
```
5. Open browser and go to: `http://127.0.0.1:5000/`

---

## 📦 Requirements
```
Flask
scikit-learn
pandas
numpy
joblib
```

---

## 🖼 Sample UI
<img width="1366" height="647" alt="Screenshot 2025-08-10 220201" src="https://github.com/user-attachments/assets/daa84004-5811-48c5-9675-4a8e1ddb8e98" />
<img width="1366" height="633" alt="Screenshot 2025-08-10 220224" src="https://github.com/user-attachments/assets/6bf67d3d-dea8-4b5f-a107-d66786eea2e6" />
<img width="1366" height="633" alt="Screenshot 2025-08-10 220241" src="https://github.com/user-attachments/assets/1fbac2c0-e6d3-4425-8255-2e0fb49ee4b0" />

---

