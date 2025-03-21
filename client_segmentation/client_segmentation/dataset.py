from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

import zipfile

from client_segmentation.config import PROCESSED_DATA_DIR
from client_segmentation.config import RAW_DATA_DIR
from client_segmentation.config import INTERIM_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR,
    inter_path: Path = INTERIM_DATA_DIR,
    output_path: Path = PROCESSED_DATA_DIR,
):

    logger.info("Processing dataset...")

    ## retrives a list of files at raw data directory
    input_files = tqdm(input_path.iterdir())

    ## just moves a file from raw into interim directory
    ## if it is compressed, then it is decompressed before
    ## moving it
    for curr_file in input_files:
        logger.info(f"Processing the file {curr_file}")

        ## hidden files are ignored
        if curr_file.name.startswith('.'):
            logger.warning(f"Ignoring the hidden file {curr_file.name}.")

        else:
            if curr_file.suffix == '.zip':
                logger.info(f"File {curr_file.name} is compressed.")

                with zipfile.ZipFile(curr_file) as zip_ref:
                    logger.info(f"Decompressing the file {curr_file.name}.")
                    zip_ref.extractall(INTERIM_DATA_DIR)

                logger.info(f"Extracted file {curr_file.name} into "
                            f"directory {INTERIM_DATA_DIR}")

            else:
                curr_file.rename(INTERIM_DATA_DIR / curr_file.name)
                logger.info(f"Moved the file {curr_file.name} into "
                            f"directory {INTERIM_DATA_DIR}.")

    logger.success("Processing dataset complete.")


if __name__ == "__main__":
    app()
