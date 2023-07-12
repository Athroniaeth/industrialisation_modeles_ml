"""
This is a boilerplate pipeline 'entrainement'
generated using Kedro 0.18.10
"""

# Import des librairies
from kedro.pipeline import Pipeline, node, pipeline
from .nodes import train

def create_pipeline(**kwargs) -> Pipeline:
    '''init pipeline'''
    return pipeline([
        node(
        func=train,
        inputs=["train_data_x", "test_data_x", "train_data_y","test_data_y"],
        outputs="train_model",
        name="node_model_data"
        )
    ])