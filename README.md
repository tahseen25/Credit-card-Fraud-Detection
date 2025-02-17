# Credit Card Fraud Detection

This project aims to build a machine learning model to detect fraudulent credit card transactions. The dataset used for this project contains transaction details, and the model is trained to distinguish between legitimate and fraudulent transactions.

---

## Dataset

The dataset contains the following columns:
- **Time**: Number of seconds elapsed between this transaction and the first transaction in the dataset.
- **V1, V2, ..., V28**: Principal components obtained with PCA.
- **Amount**: Transaction amount.
- **Class**: Target variable (0 for legitimate transactions, 1 for fraudulent transactions).

> 📂 **Note:** Ensure the dataset file is in the project directory. If the dataset is public, you can provide the download link here.

---

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/credit-card-fraud-detection.git
    cd credit-card-fraud-detection
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1. **Ensure you have the dataset file in the project directory.**

2. **Run the Jupyter Notebook or Python script to train and evaluate the model:**
    ```bash
    jupyter notebook Credit_Card_Fraud_Detection.ipynb
    ```
    or
    ```bash
    python credit_card_fraud_detection.py
    ```

---

## Model Training

1. **Load and explore the dataset.**
2. **Preprocess the data, handle missing values, and balance the dataset.**
3. **Split the data into training and testing sets.**
4. **Train a logistic regression model using the training data.**

---

## Model Evaluation

- Evaluate the model on both training and testing datasets.
- Calculate accuracy scores and other performance metrics.

---

## Visualization

- Visualize the distribution of classes before and after under-sampling.
- Analyze feature distributions for normal and fraudulent transactions.
- Visualize model performance metrics.

---

## Results

- The model achieved an accuracy of **94%** on the training set and **Y%** on the test set.
- Key insights and findings from the data and model are documented in the notebook.

---

## Screenshots
![Screenshot 2024-04-24 195455](https://github.com/user-attachments/assets/386f61f1-ae66-4a3c-a49f-7b8dca62baf6)

![Screenshot 2024-04-24 195721](https://github.com/user-attachments/assets/dff45f30-0f23-48f1-896f-3e22f3c4bf53)

![Screenshot 2024-04-24 195924](https://github.com/user-attachments/assets/4f799a98-a4e9-4cf1-a785-cedcf46d25d5)


## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the repository.**
2. **Create a new branch:**
    ```bash
    git checkout -b feature-branch
    ```
3. **Make your changes and commit them:**
    ```bash
    git commit -m 'Add some feature'
    ```
4. **Push to the branch:**
    ```bash
    git push origin feature-branch
    ```
5. **Submit a pull request.**

---

