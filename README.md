# nba_classifier
The aim of this project is to predict which players are likely to play at least 5 years in NBA, in order to help recruiters choose the best players

The project includes 7 files :
- nba_logreg.csv : the data
- nba_nn.mdl : the machine learning model that performs classification
- nba.scaler : the model that performs the scaling of the data
- NBA.ipynb : the jupyter notebook that shows the path that lead me to choose this model
- app.py : the API that receives a json file stating the data of a player and returns a prediction
- user_interface.py : the file that the customer has to fill to get a prediction
- requirements.txt : the requirements file

In order to get a prediction, one should run the app.py file and then execute user_interface.py after having modified the parameters of the player
