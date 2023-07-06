# Import des librairies
from kedro.pipeline import node
from kedro.framework.project import settings
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import regularizers

def train_bis(train_df_x: pd.DataFrame, test_df_x: pd.DataFrame, train_df_y: pd.DataFrame, test_df_y: pd.DataFrame):
    import mlflow

    mlflow.autolog()

    with mlflow.start_run() as run:
        model = create_model(input_shape=(7,1))
        history = model.fit(train_df_x, train_df_y, epochs=100, validation_data=(test_df_x, test_df_y), steps_per_epoch=1000)
        
        predictions = model.predict(test_df_x)
        print(predictions)

    return model

    import os
    from random import random, randint
    from mlflow import log_metric, log_param, log_params, log_artifacts
    import mlflow
    from mlflow.models.signature import infer_signature
    from sklearn.model_selection import train_test_split

    #print(history.history)
    #log_metric("accuracy", history.history["categorical_accuracy"])
    #log_metric("loss", history.history["loss"])

    # Log an artifact (output file)
    #if not os.path.exists("outputs"):
    #    os.makedirs("outputs")
#
    #with open("outputs/test.txt", "w") as f:
    #    f.write("hello world!")
#
    #log_artifacts("outputs")

    return model

#def train_model(train_df_x, test_df_x, train_df_y, test_df_y):
#    # Il faut vérifier que les données ont le même nombre d'entrée
#    # Ce code ne fonctionne pas car il 'y as pas le même nombre de donnée (8000vs2000)
#    # assert train_x.shape == train_y.shape, f"{train_x.shape} {train_y.shape}"
#    with mlflow.start_run() as run:
#        train_df_x = train_df_x.to_numpy()
#        train_df_y = train_df_y.to_numpy()
#        # assert test_x.shape == test_y.shape
#        train_df_x = train_df_x.reshape((8000, 7, 1))
#        train_df_y = train_df_y.reshape((8000, 7, 1))
#
#        print(train_df_x.shape[1:])
#
#        print(train_df_x.shape, train_df_y.shape)
#
#        model = create_model(train_df_x.shape[1:])
#        history = model.fit(train_df_x, train_df_y, validation_data=(test_df_x, test_df_y))
#
#        predictions = model.predict(X_test)
#
#        print(predictions)
#        signature = infer_signature(X_test, predictions)
#        mlflow.sklearn.log_model(rf, "model", signature=signature)
#        print("Run ID: {}".format(run.info.run_id))
#        print(history)

# Création du modèle d'entraînement
def create_model(input_shape, units=192, activation='relu', l2_value=0.01, dropout_rate=None, learning_rate=1e-3):
    
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

    if dropout_rate is not None:
        x = layers.Dropout(dropout_rate)(x)
    
    x = layers.Dense(input_shape[0], activation='sigmoid')(x)
        
    #Création du modèle
    model = tf.keras.Model(inputs=inputs, outputs=x)
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                  loss=[tf.keras.losses.MeanSquaredError()], metrics=[tf.keras.metrics.CategoricalAccuracy()])
    
    return model