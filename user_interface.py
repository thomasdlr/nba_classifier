# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 11:17:38 2021

@author: thoma
"""

import requests

def predict_player():
    
    """
    This function displays the prediction of the API for the player caracterized by the data
    diplayed in the body variable
    
    :return response.json() : the prediction of the model in the following format : "label : meaning of the label"
    """
    
    url = 'http://127.0.0.1:1234/predict'  # localhost and the defined port + endpoint
    body = {
        "GP" : 36., #games played
        "MIN": 27.4, #minutes played
        "PTS": 7.4, #points per game
        'FGM': 2.6, #field goals made
        'FGA': 7.6, #field goal attempts
        'FG%': 34.7, #field goal percent
        '3P Made': 0.5, #3 points made
        '3PA': 2.1, # 3 points attempts
        '3P%': 25, # 3 points percent
        'FTM': 1.6, #free throw made
        'FTA': 2.3, #free throw attempts
        'FT%': 69.9, #free throw percent
        'OREB': 0.7, #offensive rebounds
        'DREB': 3.4, #defensive rebounds
        'REB': 4.1, #rebounds
        'AST': 1.9, #assists
        'STL': 0.4, #steals
        'BLK': 0.4, #blocks
        'TOV': 1.3, #turnovers
    }

    response = requests.post(url, data=body)
    return response.json()

if __name__ == "__main__":
    predict_player()