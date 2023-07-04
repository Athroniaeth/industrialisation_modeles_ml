# Import des librairies
from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train_bis

def create_pipeline(**kwargs) -> Pipeline:
    '''init pipeline'''
    return pipeline([
        node(
        func=train_bis,
        inputs=["train_data_x", "test_data_x", "train_data_y","test_data_y"],
        outputs="ml_model",
        name="node_model_data"
        )
    ])