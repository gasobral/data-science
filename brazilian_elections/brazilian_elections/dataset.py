from pathlib import Path
import zipfile

from loguru import logger
from tqdm import tqdm
import pandas as pd
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

            if curr_file.suffix not in {".pqt", ".pgt", ".parquet"}:
                logger.info(f"Converting the file {curr_file.name} "
                            f"in parquet format.")
                curr_file_df = pd.read_csv(curr_file)
                file_name = curr_file.name.replace(curr_file.suffix,
                                                   ".pqt")
                curr_file_df.to_parquet(PROCESSED_DATA_DIR / file_name,
                                        engine='pyarrow')

    logger.success("Processing dataset complete.")


if __name__ == "__main__":
    app()
