from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Load the dataset
credit_card_data = pd.read_csv('credit_data.csv')

# Separate the data for analysis
legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]

legit_sample = legit.sample(n=492)

new_dataset = pd.concat([legit_sample, fraud], axis=0)

X = new_dataset.drop(columns='Class', axis=1)
Y = new_dataset['Class']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Train the Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, Y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    features = [float(request.form[f'feature{i+1}']) for i in range(30)]
    prediction = model.predict([features])[0]

    if prediction == 0:
        result = 'Legitimate Transaction'
    else:
        result = 'Fraudulent Transaction'

    return render_template('result.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
