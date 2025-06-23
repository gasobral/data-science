from pathlib import Path

import typer
from loguru import logger
from tqdm   import tqdm

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from client_segmentation.config import FIGURES_DIR
from client_segmentation.config import PROCESSED_DATA_DIR
from client_segmentation.config import CUSTOMER_WITH_LABELS

app = typer.Typer()


def numerical_analysis(numerical_data: pd.DataFrame,
                       plot_path: Path):
    """
Plot information about numerical data.

Arguments
---------
numerical_data: a data frame containing only numerical data.

plot_path: a path where the plot will be saved at.
    """

    fig, ax = plt.subplots(numerical_data.shape[1],
                           2,
                           figsize=(12,10))
    ax = ax.ravel()
    i = 0

    for column in numerical_data.columns:
        sns.histplot(data=numerical_data,
                     x=column,
                     ax=ax[i])
        ax[i].set_title(f'Histogram - {column}')

        sns.boxplot(data=numerical_data,
                    x=column,
                    ax=ax[i+1])
        ax[i+1].set_title(f'Boxplot - {column}')
        i += 2

    plt.tight_layout()
    plt.savefig(plot_path)


def categorical_analysis(categorical_data: pd.DataFrame,
                         plot_path: Path):
    """
Print and plot information about categorical data.

Arguments
---------
categorical_data: a data frame containing only categorical data.

plot_path: a path where the plot will be saved at.
    """

    fig, ax = plt.subplots(categorical_data.shape[1],
                           1,
                           figsize=(10, 10))

    for i, cat_col in enumerate(categorical_data.columns):
        column_data = categorical_data[cat_col].value_counts().head()
        column_data = column_data.reset_index()
        sns.barplot(data=column_data,
                    x=cat_col,
                    y='count',
                    ax=ax[i])

    plt.tight_layout()
    plt.savefig(plot_path)


@app.command()
def main(
    input_path: Path = PROCESSED_DATA_DIR / CUSTOMER_WITH_LABELS,
    output_path: Path = FIGURES_DIR
):

    logger.info(f"Generating plot from data {input_path}")
    customer_data = pd.read_csv(input_path)
    labels = customer_data['cluster_label'].unique()

    ## plot graphs for each label (cluster label)
    for label in tqdm(labels):
        logger.info(f"Plotting data for label {label}")
        mask = customer_data['cluster_label'] == label
        customer_labeled = customer_data[mask]
        ## plot graphs for numerical variables
        num_cols = customer_labeled.select_dtypes(include='number').\
            columns.to_list()
        ## cluster label is removed since its value is the same for all
        ## customers
        num_cols.remove('cluster_label')
        file_name = f'numerical_data_label{label}.png'
        numerical_analysis(customer_labeled[num_cols],
                           FIGURES_DIR / file_name)
        logger.info(f"Ploted numerical data at "
                    f"{FIGURES_DIR / file_name}")

        ## plot graphs for categorical variables
        cat_cols = customer_labeled.select_dtypes(include='object').\
            columns.to_list()
        file_name = f'categorical_data_label{label}.png'
        categorical_analysis(customer_labeled[cat_cols],
                             FIGURES_DIR / file_name)
        logger.info(f"Ploted categorical data at "
                    f"{FIGURES_DIR / file_name}")

    logger.success("Plot generation complete.")


if __name__ == "__main__":
    app()
