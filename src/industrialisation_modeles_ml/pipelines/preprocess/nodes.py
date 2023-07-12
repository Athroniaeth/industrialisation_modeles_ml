"""
This is a boilerplate pipeline 'preprocess'
generated using Kedro 0.18.10
"""

# Import des librairies
import os
import yaml
import pandas as pd
from sklearn.model_selection import train_test_split
from kedro.pipeline import node
from kedro.config import ConfigLoader
from kedro.framework.project import settings


def clean_data(clean_data: pd.DataFrame) -> pd.DataFrame:
    # Vérification des valeurs nulles -> suppresion des lignes (alerte)
    null_values = clean_data.isnull()

    # Utilisez la méthode any(axis=1) pour identifier les lignes contenant des valeurs nulles
    rows_with_nulls = null_values.any(axis=1)

    # Parcourez les lignes avec des valeurs nulles et affichez un avertissement pour chaque ligne
    for index, row in clean_data[rows_with_nulls].iterrows():
        print(f"Avertissement : La ligne {index} contient des valeurs nulles.")
        print(row)

    return clean_data.dropna()


def normalise_data(clean_data: pd.DataFrame) -> pd.DataFrame:
    # Mise à l'échelle des données -> suppresion des lignes (alerte)
    min_values = clean_data.min().min()
    max_values = clean_data.max().min()

    # Les fichiers yaml ne supporte pas les objets numpy & ConfigLoader ne peut pas écrire dans des fichiers yml sans erreurs
    # https://stackoverflow.com/questions/33794873/yaml-dump-throws-an-error-on-numpy-array-type-attribute-of-an-object-in-python
    config_path = f"{os.getcwd()}\\conf\\base\\parameters\\preprocess.yml"
    config_dict = {"min_values": float(min_values), "max_values": float(max_values)}

    with open(config_path, 'w') as file:
        yaml.dump(config_dict, file, default_flow_style=False)

    # Formule de normalisation MinMaxScaler
    clean_data = (clean_data - min_values) / (max_values - min_values)

    return clean_data


def split_data(clean_data: pd.DataFrame):
    # Récupération de 20% des données pour le test du modèle
    dfx = clean_data.loc[:, ['before_exam_125_Hz', 'before_exam_250_Hz', 'before_exam_500_Hz', 'before_exam_1000_Hz', 'before_exam_2000_Hz', 'before_exam_4000_Hz', 'before_exam_8000_Hz']]
    dfy = clean_data.loc[:, ['after_exam_125_Hz', 'after_exam_250_Hz', 'after_exam_500_Hz', 'after_exam_1000_Hz', 'after_exam_2000_Hz', 'after_exam_4000_Hz', 'after_exam_8000_Hz']]
    train_df_x, test_df_x, train_df_y, test_df_y = train_test_split(dfx, dfy, test_size=0.2)

    return train_df_x, test_df_x, train_df_y, test_df_y