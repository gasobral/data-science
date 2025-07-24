from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

try:
    from music_popularity.config import PROCESSED_DATA_DIR
    from music_popularity.config import RAW_DATA_DIR
    from music_popularity.config import DATABASE_FILE
    from music_popularity.config import DATASET_URL

except:
    from config import PROCESSED_DATA_DIR
    from config import RAW_DATA_DIR
    from config import DATABASE_FILE
    from config import DATASET_URL

app = typer.Typer()


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR,
    output_path: Path = PROCESSED_DATA_DIR,
    database: Path = DATABASE_FILE,
    dataset_url: str = DATASET_URL
):
    """
Extract the data from Kaggle, load them into a database and perform
some data cleaning/transformation.

Arguments
---------
    input_path: a Path object which points to raw data directory.
    output_path: a Path object at which the data will be saved to.
    database: a Path object that contains database directory.
    """

    logger.info("Checking if it is needed to extract data!")
    matched_files = [csv_file for csv_file in input_path.glob("*.csv")]\
        + [json_file for json_file in input_path.glob("*.json")]

    if len(matched_files) == 0:
        logger.info(f"No csv or json files were found at\n{input_path}")

        ## downloading files from Kaggle
        try:
            import kagglehub

            dl_path = kagglehub.dataset_download(DATASET_URL)
            logger.success(f"Downloaded the dataset at directory {dl_path}\n")
            dl_dir = Path(dl_path)

            ## after downloading the data set, move the csv files to
            ## raw data directory
            input_files = tqdm(dl_dir.glob("*.csv"))

            for input_file in input_files:
                logger.info(f"Moving the file {input_file} to "
                            f"{input_path / input_file.name}\n")
                input_file.replace(input_path / input_file.name)

        except Exception as e:
            logger.error(f"{e}")
            logger.error("No files were processed!")

    else:
        logger.info(f"The following files were found at\n{input_path}")

        for matched_file in matched_files:
            logger.info(matched_file.name)

        for matched_file in tqdm(matched_files, total=len(matched_files)):
            logger.info(f"Processing the file {matched_file.name}")

        logger.success("Processing dataset complete.")


if __name__ == "__main__":
    app()
