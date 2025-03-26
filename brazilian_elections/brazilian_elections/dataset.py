from pathlib import Path
import zipfile

from loguru import logger
from tqdm import tqdm
import typer

try:
    from config import PROCESSED_DATA_DIR
    from config import RAW_DATA_DIR

except ModuleNotFoundError:
    from brazilian_elections.config import PROCESSED_DATA_DIR
    from brazilian_elections.config import RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR,
    output_path: Path = PROCESSED_DATA_DIR,
):

    logger.info("Processing dataset...")

    # creates a list of files to be processed
    input_files = tqdm(input_path.iterdir())

    for curr_file in input_files:
        logger.info(f"Processing the file {curr_file}.")

        if curr_file.name.startswith('.'):
            logger.warning(f"Ignoring hiddne file {curr_file.name}")

        else:
            if curr_file.suffix == '.zip':
                logger.info(f"File {curr_file.name} is compressed.")

                with zipfile.ZipFile(curr_file) as zip_ref:
                    logger.info(f"Decompressing the file {curr_file.name}")
                    zip_ref.extractall(PROCESSED_DATA_DIR)

                logger.info(f"Extracted file {curr_file.name} into "
                            f"directory {PROCESSED_DATA_DIR}")
            else:
                curr_file.rename(PROCESSED_DATA_DIR / curr_file.name)
                logger.info(f"Moved the file {curr_file.name} into "
                            f"directory {PROCESSED_DATA_DIR}.")

    logger.success("Processing dataset complete.")


if __name__ == "__main__":
    app()
