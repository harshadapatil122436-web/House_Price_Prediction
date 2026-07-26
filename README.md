House Price Prediction

A simple ML-powered web app that predicts house prices in Bangalore based on location, square footage, number of bedrooms, and bathrooms. The backend is a Flask REST API, and I've tested it thoroughly using Postman before hooking up the frontend.

About the project

I built this to get hands-on experience with the full pipeline of a machine learning project — from cleaning a raw dataset, training a regression model, and saving it as a reusable artifact, to exposing predictions through an API and finally connecting it to a UI.

The dataset is the Bangalore House Price Data set from Kaggle. After cleaning it up and doing some feature engineering (mainly around location one-hot encoding and outlier removal), I trained a model and saved it using pickle so the Flask server can load it at runtime without retraining every time.

Project structure
Sever/ - the Flask backend (server.py has the routes, util.py loads the model and runs predictions)
Sever/artifact/ - the saved model file and column data it needs to run
model/ - where I did the data cleaning and trained the model
client/ - frontend
postman/ - Postman collection I used to test the API
Tech used
Python, Flask
scikit-learn, NumPy, pandas
Postman (for testing the API while building it)
Git/GitHub
Running it locally

You'll need Python 3 installed.

bash
git clone https://github.com/harshadapatil122436-web/House_Price_Prediction.git
cd House_Price_Prediction

python -m venv venv
venv\Scripts\activate

pip install flask numpy pandas scikit-learn

cd Sever
python server.py

Once it's running, the API will be live at http://127.0.0.1:5000.

API

GET /get_location_names Returns all the locations the model knows about, so the frontend can populate a dropdown.

json
{
  "locations": ["1st Phase JP Nagar", "Whitefield", "..."]
}

POST /predict_home_price Takes the house details and returns an estimated price. Sent as x-www-form-urlencoded:

Field	Example
total_sqft	1000
location_name	1st Phase JP Nagar
bhk_price	2
bath_price	2
json
{
  "estimated_price": 83
}

(Prices are in lakhs, matching the scale of the original dataset.)

Testing

I used Postman to test both endpoints while building this — there's a collection in the postman/ folder if you want to try it yourself. Just make sure server.py is running first, otherwise the requests will fail to connect.

What's next

Still working on:

Finishing up the frontend so it's actually usable end to end
Handling bad input a bit more gracefully (right now it'll throw an error on missing fields)
Maybe deploying it somewhere so it's not just local
Author

Harshada Patil
