import pandas as pd
import numpy  as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline      import Pipeline
from sklearn.compose       import ColumnTransformer


## Declare data structures - - - - - - - - - - - - - - - - - - - - - - #
## defines the pipeline to be applied in data pipeline
categorical_pipeline = Pipeline(
    steps=[
        ('encoder', OrdinalEncoder(dtype=np.int64))
    ]
)

numerical_pipeline = Pipeline(
    steps=[
        ('scaler', RobustScaler())
    ]
)


## Functions - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def init_data_pipeline(df : pd.DataFrame):
    """
Given a data frame, returns a ColumnTransformer to be used for
preprocessing the data.

Arugments
---------
df: a data frame with customer data

Return
------
A ColumnTransformer object to be use for preprocessing.
    """

    num_cols = df.select_dtypes(include='number').columns.to_list()
    cat_cols = df.select_dtypes(include='object').columns.to_list()

    preprocessing = ColumnTransformer(
        transformers=[
            ('num_transform', numerical_pipeline, num_cols),
            ('cat_transform', categorical_pipeline, cat_cols)
        ],
        remainder='passthrough'
    )

    return preprocessing
