"""
This is a boilerplate pipeline 'deploiement'
generated using Kedro 0.18.10
"""
import os
import pickle

import pandas
import yaml
from flask import Flask, request
from kedro.framework.session import KedroSession

app = Flask(__name__)


# Define Flask route for POST requests

@app.route('/train', methods=['GET'])
def train():
    # Récupérer le fichier CSV envoyé dans la requête
    fichier_csv = request.files['fichier_csv']

    fichier_csv.save('data/01_raw/flask_data' + fichier_csv.filename)

    with KedroSession.create("industrialisation_modeles_ml", project_path=".") as session:
        session.run(pipeline_name="preprocess",  # Le nom du pipe à exécuter
        )

    with KedroSession.create("industrialisation_modeles_ml", project_path=".") as session:
        model_input = session.run(pipeline_name="entrainement",  # Le nom du pipe à exécuter
        )

    model_input.to_csv("data/05_model_input/predict_data.csv")

    return "Entrainement terminée"


@app.route("/predict", methods=["GET"])
def predict():
    # Chargez le modèle depuis le fichier pickle
    with open(f"{os.getcwd()}\\data\\06_models\\train_model.pickle", 'rb') as file:
        model = pickle.load(file)

    normalised_data = pandas.read_csv("data/05_model_input/predict_data.csv")

    predictions = model.predict(normalised_data)

    # Chemin du fichier YML pour avoir le max et min du MinMaxScaler
    config_path = f"{os.getcwd()}\\conf\\base\\parameters\\preprocess.yml"

    # Chargement du fichier YML
    with open(config_path, 'r') as file:
        content = yaml.safe_load(file)

    min_values = content['min_values']
    max_values = content['max_values']

    # Formule pour dénormalisé les données
    denormalised_data = predictions(max_values - min_values) + min_values

    # Sauvegarde les données
    output = denormalised_data.to_csv('data/07_model_outpout.csv')

    return output.to_json(orient='records')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
