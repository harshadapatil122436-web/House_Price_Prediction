from flask import Flask, request, jsonify
import util

app = Flask(__name__)
util.load_saved_artifacts()

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location_name = request.form['location_name']
    bhk = int(request.form['bhk_price'])
    bath = int(request.form['bath_price'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location_name, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print('Starting Python Flask Server for House Price Prediction')
 
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


