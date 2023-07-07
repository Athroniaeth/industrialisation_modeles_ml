# Import des librairies
import pandas as pd

from flask import Flask, request, jsonify


# Définition de la route Flask pour les requêtes POST
app = Flask(__name__)
@app.route("/predict", methods=["POST"])

def predict():
    #Définition du chemin d'accès au fichier pour enregistrer les données de la requête POST
    filepath = "data/08_reporting/"
    
    #Enregistrement des données de la requête POST dans un fichier JSON
    save_from_post_request(request, filepath)
    
    with KedroSession.create("sound", project_path=".") as session:
        create_pipeline = session.run(
            pipeline_name = "entrainement", #Nom du pipe à exécuter
            )
        output = pd.read_csv('where_my_data_are_suppose_to_be_saved')
        
        return output.to_json(orient='records')

# Lancement du serveur Flask
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=False)