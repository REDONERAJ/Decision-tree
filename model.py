import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import joblib

diabetes = load_diabetes(as_frame=True)
df = diabetes.frame

df['age'] = (df['age'] * 20) + 50      
df['bmi'] = (df['bmi'] * 8) + 25       
df['bp'] = (df['bp'] * 25) + 80        
df['s5'] = df['s5'] * 1.2 + 4.5         
df['s1'] = df['s1'] * 0.1 + 0.05       

X = df[['age', 'bmi', 'bp', 's5', 's1']]
y = df['target']  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, 'decision_tree_diabetes.pkl')
