import pandas as pd
import numpy  as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline      import Pipeline
from sklearn.compose       import ColumnTransformer


## Declare data structures - - - - - - - - - - - - - - - - - - - - - - #
## defines the pipeline to be applied in data pipeline
## pipeline for categorical variables
categorical_pipeline = Pipeline(
    steps=[
        ('encoder', OrdinalEncoder(dtype=np.int64))
    ]
)

## pipeline for numerical variables
numerical_pipeline = Pipeline(
    steps=[
        ('scaler', RobustScaler())
    ]
)


## Functions - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def init_pipeline(num_cols: list, cat_cols: list):
    """
Given list with numerical and categorical variables, returns a
ColumnTransformer to be used for preprocessing the data.

Arugments
---------
num_cols: a list with the names of numerical variables

cat_cols: a list with the names of categorical variables

Return
------
A ColumnTransformer object to be use for preprocessing.
    """

    preprocessing = ColumnTransformer(
        transformers=[
            ('num_transform', numerical_pipeline, num_cols),
            ('cat_transform', categorical_pipeline, cat_cols)
        ],
        remainder='passthrough'
    )

    return preprocessing
