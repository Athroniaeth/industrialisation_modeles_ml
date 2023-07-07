# Import des librairies
from .nodes import predict

from kedro.pipeline import Pipeline, node, pipeline

def create_pipeline(**kwargs) -> Pipeline:
    '''Initialisation de la pipeline'''
    return pipeline([
        node(
        func=predict,
        inputs="ml_model",
        outputs="predict_model",
        name="node_predict_model_data"
        )
    ])