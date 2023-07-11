"""Sound
"""

__version__ = "0.1"

import os
# Get the current working directory
project_dir = os.path.abspath(os.curdir)

# Define the model directory
model_dir = os.path.join(project_dir, "data", "06_models")

# Define the MLflow tracking URI
os.environ["MLFLOW_TRACKING_URI"] = "file://{}".format(model_dir)