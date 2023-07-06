import pytest
import pandas as pd
import mlflow
from sklearn.metrics import mean_squared_error
from math import sqrt

# regarde si la fonction d'entrainement est celle 
# que nous avions déterminé avec < 75% d'accuracy
def test_model():
    test_df_x = pd.read_csv("data/05_model_input/test_data_x.csv")
    test_df_y = pd.read_csv("data/05_model_input/test_data_y.csv")

    test_df_x = test_df_x.to_numpy()
    test_df_y = test_df_y.to_numpy()
    # assert test_x.shape == test_y.shape
    test_df_x = test_df_x.reshape((-1, 7, 1))
    test_df_y = test_df_y.reshape((-1, 7, 1))
    # Vérification de l'accuracy

    model = mlflow.tensorflow.load_model('runs:/863762eb9d394c40ae44cdc8b68c8151/')
    predictions = model.predict(test_df_x)

    print(predictions.shape, test_df_y.shape)

    test_df_y = test_df_y.reshape(-1, 7)
    # Calcul du %erreurs root-mean-square
    mse = mean_squared_error(predictions, test_df_y)
    
    assert mse < 0.1, "Le modèle n'est pas performent (erreur supérieur à 10%)"

pytest.main()