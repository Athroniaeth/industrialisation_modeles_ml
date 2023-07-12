"""
This is a boilerplate pipeline 'preprocess'
generated using Kedro 0.18.10
"""

# Import des librairies
from kedro.pipeline import Pipeline, node, pipeline
from .nodes import clean_data, normalise_data, split_data


def create_pipeline(**kwargs) -> Pipeline:
    '''init pipeline'''
    return pipeline([
        node(
            func=clean_data,
            inputs="raw_data",
            outputs="clean_data",
            name="node_clean_raw_data"
        ),

        node(
            func=normalise_data,
            inputs="clean_data",
            outputs="normalised_data",
            name="node_normalise_clean_data"
        ),

        node(
            func=split_data,
            inputs="normalised_data",
            outputs=["train_data_x", "test_data_x", "train_data_y", "test_data_y"],
            name="node_split_data"
        )
    ])
