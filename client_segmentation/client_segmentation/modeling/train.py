from pathlib import Path

import typer
import pandas as pd
from loguru import logger
from tqdm   import tqdm

from sklearn.cluster import AgglomerativeClustering

from client_segmentation.config import MODELS_DIR
from client_segmentation.config import PROCESSED_DATA_DIR
from client_segmentation.config import CUSTOMER_BUY_DATA
from client_segmentation.config import CUSTOMER_WITH_LABELS

from client_segmentation.modeling.pipeline import init_pipeline

app = typer.Typer()


@app.command()
def main(
    features_path: Path = PROCESSED_DATA_DIR / CUSTOMER_BUY_DATA,
    labels_path: Path = PROCESSED_DATA_DIR / CUSTOMER_WITH_LABELS
):
    """
Trains a clustering algorithm, obtain the clusters where customers are
located at and exports this data into a csv file pointed by labels_path.

Arguments
---------
features_path: a path where a csv file, which the features, is located at.

labels_path: a path where is exported a csv file with custome and cluster
             labels, identifying to which cluster (group) a customer
             belongs to.
    """

    logger.info("Training some model...")
    logger.info(f'Reading data from {features_path}')
    features = pd.read_csv(features_path)

    ## impute values before applying the encoders
    features['product_category_name'] = features['product_category_name'].\
        fillna('categoria_ausente')

    ## pipeline execution
    num_cols = features.select_dtypes(include='number').columns.\
        to_list()
    cat_cols = features.select_dtypes(include='object').columns.\
        to_list()
    processing = init_pipeline(num_cols, cat_cols)
    features_transformed = processing.fit_transform(features)
    features_transformed = pd.DataFrame(data=features_transformed,
                                        columns=num_cols+cat_cols)

    logger.info(f"Sample of transformed data:\n"
                f"{features_transformed.head()}")

    ## training a clustering model
    clustering_model = AgglomerativeClustering(n_clusters=2,
                                               linkage='ward')

    ## we train the model only in 20% of data due to memory issues
    chunk_size = int(features_transformed.shape[0] * 0.2)
    sample = features_transformed.sample(n=chunk_size)

    ## obtain cluster labels for each instance
    cluster_labels = clustering_model.fit_predict(sample)

    ## creates a data frame with the labels and export it to
    ## labels_path
    customer_with_labels = features.iloc[sample.index].copy()
    customer_with_labels['cluster_label'] = cluster_labels
    customer_with_labels.to_csv(labels_path,
                                index=False)
    logger.info(f"Exported customer data with the labels (cluster "
                f"center) to {labels_path}")

    logger.success("Modeling training complete.")


if __name__ == "__main__":
    app()
