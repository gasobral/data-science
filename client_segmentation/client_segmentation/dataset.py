from pathlib import Path
import zipfile

from loguru import logger
from tqdm import tqdm
import typer

from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline      import Pipeline
from sklearn.compose       import ColumnTransformer

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


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR,
    inter_path: Path = INTERIM_DATA_DIR,
    output_path: Path = PROCESSED_DATA_DIR,
):

    if retrieve_dataset(input_path) != 0:
        logger.error("Failed to download the dataset!\n")
        return -1

    ## TODO: executar o pré-processanmento
    ##       mover os arquivos para o diretório intermediário

    return 0


if __name__ == "__main__":
    app()
