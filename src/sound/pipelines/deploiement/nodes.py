"""
This is a boilerplate pipeline 'deploiement' generated using Kedro 0.18.10
"""

# Import des librairies
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)
# Définition de la route Flask pour les requêtes POST
@app.route("/predict", methods=["POST"])

def predict():
    # Set the filepath to save the POST request data
    filepath = "data/08_reporting/"
    
    # Save data from POST request to JSON file
    save_from_post_request(request, filepath)

    with KedroSession.create("sound", project_path=".") as session:
        create_pipeline = session.run(
            pipeline_name ="pipeline_extra", # Le nom du pipe à exécuter
            )
        output = pd.read_csv('where_my_data_are_suppose_to_be_saved')
        
        return output.to_json(orient='records')
    
    # Lance le serveur Flask
    if __name__ == '__main__':
        app.run(host='127.0.0.1', port=80, debug=False)