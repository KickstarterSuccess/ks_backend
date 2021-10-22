import pickle
import sklearn
import numpy as np
from flask_cors import CORS, cross_origin
from flask import Flask, json, request, jsonify
from .preprocessing import get_dur, get_monthyear, predict_to_string

def create_app():
    '''
    Instantiation and definition of Flask app and routes.
    '''

    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    @app.route("/")
    @cross_origin()
    
    def main():
        return "Welcome to the server!"



    @app.route("/predict", methods=["GET", "POST"])
    @cross_origin()
    def predict():
        '''
        App route for receiving front end predictive data and
        generating a prediction. Returns prediction as a string
        response.
        '''
        # Retrieve data from front end
        data = request.get_json(force=True)

        # Run feature engineering functions
        data['duration'] = get_dur(data['date'], data['deadline'])
        data['month'], data['year'] = get_monthyear(data['date'])
        # data['duration'] = 'test1'
        # data['month'], data['year'] = 'test2', 'test3'

        # Define desired variables in X_pred order
        X_vars = ['goal','month','year','duration','country','currency','category']

        # Create empty list for populating X_pred
        X_pred_list = []

        # Iterate over X_vars to populate X_pred with key value pairs
        for x in X_vars:
            X_pred_list.append(data[x])

        # Format list into 2D array for prediction
        X_pred = np.array(X_pred_list)
        X_pred = X_pred.reshape(1,-1)

        # Load locally stored pickled model
        model = pickle.load(open('ks_flask/model','rb'))
        
        # Create prediction from model
        prediction = model.predict(X_pred)

        # Covert array to string response
        prediction = predict_to_string(prediction)

        # JSONify the prediction
        prediction = jsonify({'prediction': prediction})

        # Return prediction
        return jsonify(prediction)
        

    return app