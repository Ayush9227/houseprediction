# 🏠 House Price Prediction using Linear Regression

This project demonstrates a simple machine learning application: predicting house prices based on input features such as Area (in square feet), Number of Bedrooms, and Number of Bathrooms using Linear Regression. The model is deployed as a Streamlit web application.

## 📁 Project Structure

house-price-predictor/
├── streamlit_house_price_predictor.py # Streamlit app using a pickled model
├── house_price_model.pkl # Trained Linear Regression model
├── House Price Prediction Dataset.csv # Original dataset used for training (optional)
└── README.md # Project documentation

arduino
Copy code

## 🚀 Demo

Run the live app locally using Streamlit:

```bash
streamlit run streamlit_house_price_predictor.py
🔧 Features
Predicts house price based on:

🧱 Area (square footage)

🛏 Bedrooms

🚿 Bathrooms

Trained using Scikit-Learn Linear Regression

Deployed using Streamlit

Pickle model loading for faster inference

📦 Dependencies
Install required Python packages:

bash
Copy code
pip install -r requirements.txt
📌 Sample requirements.txt:

nginx
Copy code
streamlit
pandas
numpy
scikit-learn
joblib
🧠 Model Training
The model is trained using scikit-learn’s LinearRegression on a dataset containing house prices and features. The training pipeline includes:

Selecting features: ['Area', 'Bedrooms', 'Bathrooms']

Splitting into training and test sets

Fitting the model and evaluating performance (MSE, R²)

Saving the trained model using joblib

python
Copy code
import joblib
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
joblib.dump(model, "house_price_model.pkl")
🖥 How to Use the App
Launch the app:

bash
Copy code
streamlit run streamlit_house_price_predictor.py
Enter the Area, Bedrooms, and Bathrooms using the UI sliders.

Click "Predict Price" to get an estimated house price.

📌 Example Screenshot

🧾 License
This project is open source and available under the MIT License.

🙌 Acknowledgments
Dataset: Custom dataset included as House Price Prediction Dataset.csv

Built using: Python, Scikit-Learn, Streamlit
