# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 09:04:49 2021

@author: thoma
"""

from flask import Flask
from flask_restful import Api, Resource, reqparse
import joblib
import numpy as np
from keras.models import load_model


#creation of the app
APP = Flask(__name__)
API = Api(APP)

#import of the models
NBA_SCALER = joblib.load('nba.scaler')
NBA_MODEL = load_model('nba_nn.mdl')


class Predict(Resource):

    @staticmethod
    def post():
        
        #We parse the incoming data
        parser = reqparse.RequestParser()
        paramset = ['GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3P Made', '3PA', '3P%',
       'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK',
       'TOV']
        for param in paramset:
            parser.add_argument(param)
        
        args = parser.parse_args()  # creates dict


        #We store it to a vector X_new
        X_new = np.fromiter(args.values(), dtype=float)  # convert input to array

        #dict_out stores the string that we want to desplay to the customer depending on the prediction
        dict_out={'0': "0 : This player has low chances to last five years in NBA", 
                  '1': "1 : This player has high chances to last five years in NBA"}
        
        #we make the prediction and return the corresponding string
        prediction = NBA_MODEL.predict(NBA_SCALER.transform([X_new]))[0][0]
        out = dict_out[str(int(round(prediction, 0)))]

        return out, 200
    
    
API.add_resource(Predict, '/predict')


if __name__ == '__main__':
    APP.run(debug=True, port='1234')