"""
This is a boilerplate pipeline 'Extra' generated using Kedro 0.18.10
"""

# Import des librairies
from kedro.pipeline import Pipeline, node, pipeline
from .nodes import clean_data, normalise_data, split_data

def create_pipeline(**kwargs) -> Pipeline:
    '''init pipeline'''
    return pipeline([
        node(
        func=clean_data,
        inputs="raw_daily_data",
        outputs="shaped_datas",
        name="node_clean_raw_daily_data"
        ),

        node(
        func=normalise_data,
        inputs="shaped_datas",
        outputs="norm_datas",
        name="node_norm_clean_datas"
        ),

        node(
        func=split_data,
        inputs="norm_datas",
        outputs=["train_data_x","test_data_x","train_data_y","test_data_y"],
        name="node_train_norm_datas"
        )
    ])