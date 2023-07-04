"""
This is a boilerplate pipeline 'Extra' generated using Kedro 0.18.10
"""

# Import des librairies
import yaml
import pandas as pd
from sklearn.model_selection import train_test_split

from kedro.pipeline import node
from kedro.config import ConfigLoader
from kedro.framework.project import settings

def clean_data(shaped_datas: pd.DataFrame) -> pd.DataFrame:
    #Vérification des valeurs nulles -> suppresion des lignes (alerte)
    null_values = shaped_datas.isnull()
    
    ##Utilisez la méthode any(axis=1) pour identifier les lignes contenant des valeurs nulles
    rows_with_nulls = null_values.any(axis=1)
    
    ##Parcourez les lignes avec des valeurs nulles et affichez un avertissement pour chaque ligne
    for index, row in shaped_datas[rows_with_nulls].iterrows():
        print(f"Avertissement : La ligne {index} contient des valeurs nulles.")
        print(row)
    
    return shaped_datas.dropna()

def normalise_data(shaped_datas: pd.DataFrame) -> pd.DataFrame:
    #Mise à l'échelle des données -> suppresion des lignes (alerte)
    min_values = shaped_datas.min().min()
    max_values = shaped_datas.max().min()
    
    conf_path = 'C:\\Users\\julie\\sound\\conf\\base\\parameters\\Extra.yml'
    conf_loader = ConfigLoader(conf_source=conf_path)
    
    conf_loader["min_values"] = min_values
    conf_loader["max_values"] = max_values

    with open(conf_path, 'w') as file:
        yaml.dump(conf_loader, file)

    shaped_datas = (shaped_datas - min_values) / (max_values - min_values)
    return shaped_datas

def split_data(shaped_datas: pd.DataFrame) -> pd.DataFrame:
    #Récupération de 20% des données pour le test du modèle
    dfx = shaped_datas.loc[:,['before_exam_125_Hz','before_exam_250_Hz','before_exam_500_Hz','before_exam_1000_Hz','before_exam_2000_Hz','before_exam_4000_Hz','before_exam_8000_Hz']]
    dfy = shaped_datas.loc[:,['after_exam_125_Hz','after_exam_250_Hz','after_exam_500_Hz','after_exam_1000_Hz','after_exam_2000_Hz','after_exam_4000_Hz','after_exam_8000_Hz']]
    train_df_x, train_df_y, test_df_x, test_df_y = train_test_split(dfx, dfy, test_size=0.2)

    return train_df_x