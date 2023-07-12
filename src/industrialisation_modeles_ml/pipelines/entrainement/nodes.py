"""
This is a boilerplate pipeline 'entrainement'
generated using Kedro 0.18.10
"""
import os

import yaml
from kedro.config import ConfigLoader
# Import des librairies
from kedro.pipeline import node
from kedro.framework.project import settings
import mlflow
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers


def train(train_df_x: pd.DataFrame, test_df_x: pd.DataFrame, train_df_y: pd.DataFrame, test_df_y: pd.DataFrame):
    with mlflow.start_run(run_name="last_run") as run:
        run_id = run.info.run_id

        model = create_model(input_shape=(7, 1))
        model.fit(train_df_x, train_df_y, epochs=5, validation_data=(test_df_x, test_df_y), steps_per_epoch=1000)

        print(f"Finish to train '{run_id}', save to entrainement config file.")

        config_path = f"{os.getcwd()}\\conf\\base\\parameters\\entrainement.yml"

        dict_values = {"kedro_last_run_id": run_id}

        with open(config_path, 'w') as file:
            yaml.dump(dict_values, file)

    return model


# Création du modèle d'entraînement
def create_model(input_shape, units=192, activation='relu', learning_rate=1e-3):
    # Définition de la couche d'entrée
    inputs = layers.Input(shape=input_shape)

    # Définition des couches de convolution
    # padding='same' rajoute un "pixel" à doite et à gauche pour avoir la même taille de sortie
    x = layers.Conv1D(filters=64, kernel_size=5, padding='same', activation=activation)(inputs)
    x = layers.Conv1D(filters=128, kernel_size=4, padding='same', activation=activation)(x)

    # Aplatissement des données
    x = layers.Flatten()(x)

    # Définition des couches entièrement connectées
    x = layers.Dense(units, activation='relu')(x)

    x = layers.Dense(input_shape[0], activation='sigmoid')(x)

    # Création du modèle
    model = tf.keras.Model(inputs=inputs, outputs=x)
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        loss=[tf.keras.losses.MeanSquaredError()], metrics=[tf.keras.metrics.CategoricalAccuracy()])

    return model
