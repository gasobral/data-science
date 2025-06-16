from pathlib import Path
import zipfile

from loguru import logger
from tqdm import tqdm
import typer

import pandas as pd
import numpy  as np

## imports directory configuration
from client_segmentation.config import PROCESSED_DATA_DIR
from client_segmentation.config import RAW_DATA_DIR
from client_segmentation.config import INTERIM_DATA_DIR

## imports the data mapping for the csv files from Olist data set
from client_segmentation.config import olist_customers_dataset_map
from client_segmentation.config import olist_order_reviews_dataset_map
from client_segmentation.config import olist_order_reviews_dataset_map
from client_segmentation.config import olist_orders_dataset_map
from client_segmentation.config import olist_order_payments_dataset_map
from client_segmentation.config import olist_order_items_dataset_map
from client_segmentation.config import olist_products_dataset_map
from client_segmentation.config import olist_geolocation_dataset_map
from client_segmentation.config import olist_sellers_dataset_map
from client_segmentation.config import product_category_name_translation_map
from client_segmentation.config import data_mapping


app = typer.Typer()


## Functions - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def retrieve_dataset(input_path: Path = RAW_DATA_DIR) -> int:
    """
Retrives the Olist data set from Kaggle, if the csv files are not at
raw directory.

Arguments
---------
input_path: a Path object poting to raw data directory.

Return
------
The function returns 1 if any error happens, otherwise, it returns 0.
    """

    ## retrieves the csv files at raw directory
    csv_files = [csv_file.name.split('.')[0]
                 for csv_file in input_path.glob("*.csv")]

    ## check if all required csv files are at raw directory
    ## note that the keys from the dictionary data_mapping forms
    ## a list of all csv files from Olist data set
    csv_files_status = [required_csv in csv_files
                        for required_csv in data_mapping.keys()]

    ## if all required csv files were found, then no action is required
    if all(csv_files_status):
        logger.info("All required csv files are at raw directory. It is"
                    " not needed to download the data set.")
        return 0

    ## if any csv file is missing, then the data set is download from
    ## Kaggle
    else:
        logger.info("Some csv files are missing, then the data set"
                    " will be donwloded from Kaggle.")
        try:
            import kagglehub

            dl_path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
            logger.success(f"Downloaded the dataset at directory {dl_path}\n")
            dl_dir = Path(dl_path)

            ## after downloading the data set, move the csv files to
            ## raw data directory
            input_files = tqdm(dl_dir.glob("*.csv"))

            for csv_file in input_files:
                logger.info(f"Moving the file {csv_file} to "
                            f"{input_path / csv_file.name}\n")
                csv_file.replace(input_path / csv_file.name)

            return 0

        except Exception as e:
            print(e)
            return -1


def data_aquisition(file_path: Path,
                    data_mapping: dict) -> pd.DataFrame:
    """
    Given a path to a csv file, returns a data frame with the data from
    the csv file.
    
    Arguments
    ---------
    file_path: a file path of a csv file.
    
    data_mapping: a dictionary with a mapping, which tells type of data
                  for each column of csv file.

    Return
    ------
    A data frame with the data loaded from csv file.
    """

    ## create file without file extention (suffix) in order to
    ## obtain the date mapping for dataset columns 
    name_suffixless = file_path.name.split('.')[0]
    dataset = pd.read_csv(file_path,
                          dtype=data_mapping[name_suffixless],
                          date_format="%Y-%m-%d %H:%M:%S")

    ## creates a list only with the columns which contain data on
    ## their name
    date_columns = [col for col in dataset.columns
                    if "date" in col or
                    "time" in col or
                    "order_approved_at" in col]

    if len(date_columns) != 0:
        for col in date_columns:
            dataset[col] = pd.to_datetime(dataset[col],
                                          format="%Y-%m-%d %H:%M:%S")
    else:
        print("Data set has no columns which contain date!"
              " No parsing required.")

    return dataset


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR,
    inter_path: Path = INTERIM_DATA_DIR,
    output_path: Path = PROCESSED_DATA_DIR,
):
    """
Loads the data set from Kaggler into raw directory and export them into
intermediate directory.
    """

    ## retreives the data set from Kaggle
    if retrieve_dataset(input_path) != 0:
        logger.error("Failed to download the dataset!\n")
        return -1

    ## once they data set is downloaded, load the data (parsin
    ## date columns) and move them to intermediate directory
    logger.info("Loading the data set from raw directory...")

    for csv_file in input_path.glob("*.csv"):
        df_raw_data = data_aquisition(csv_file, data_mapping)
        df_raw_data.to_csv(INTERIM_DATA_DIR / csv_file.name,
                           index=False,
                           date_format="%Y-%m-%d %H:%M:%S")
        logger.info(f"Exported loaded data from {csv_file} "
                    f"to {INTERIM_DATA_DIR / csv_file.name}")

    return 0


if __name__ == "__main__":
    app()
