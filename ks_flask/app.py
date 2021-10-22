import pickle
from flask_cors import cross_origin
from flask import Flask, request, jsonify
from .preprocessing import get_dur, get_monthyear, predict_to_string

def create_app():
    '''
    Instantiation and definition of Flask app and routes.
    '''

    app = Flask(__name__)

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
        data = request.get_json()

        # # Run feature engineering functions
        # data['duration'] = get_dur(data['launch'], data['deadline'])
        # data['month'], data['year'] = get_monthyear(data['launch'])

        # # Define desired variables in X_pred order
        # X_vars = ['goal','month','year','duration','country','currency','category']

        # # Create empty list for populating X_pred
        # X_pred = []

        # # Iterate over X_vars to populate X_pred with key value pairs
        # for x in X_vars:
        #     X_pred.append(data[x])

        # # Load locally stored pickled model
        # model = pickle.load(open('model','rb'))

        # # Create prediction from model
        # prediction = model.predict(X_pred)

        # # Covert array to string response
        # prediction = predict_to_string(prediction)

        # # JSONify the prediction
        # prediction = jsonify({'prediction': prediction})

        test = {'name':1, 'country':2}
        # Return prediction (may need reformatting)
        return test

    @app.route("/test", methods=["GET", "POST"])
    @cross_origin()
    def test():
        dummydata = {'name':1, 'country':2}
        return jsonify(dummydata)

    return app