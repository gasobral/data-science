from pathlib import Path

import typer
import sqlite3
from loguru import logger
from tqdm   import tqdm

import sqlite3
import pandas as pd

from client_segmentation.config import PROCESSED_DATA_DIR
from client_segmentation.config import SQL_DIR
from client_segmentation.config import DATABASE
from client_segmentation.config import SQL_CUSTOMER_BUY_DATA
from client_segmentation.config import CUSTOMER_BUY_DATA

app = typer.Typer()


@app.command()
def main(
    database_path: Path = PROCESSED_DATA_DIR / DATABASE,
    output_path: Path = PROCESSED_DATA_DIR,
    sql_path: Path = SQL_DIR / SQL_CUSTOMER_BUY_DATA,
    csv_path: Path = PROCESSED_DATA_DIR / CUSTOMER_BUY_DATA
):
    """
Executes a SQL query to extract all the data related to customers and
exports them into a csv file.

Arguments
---------
database_path: a path which points to database location.

output_path: a path at which the features will be exported to.

sql_path: a path containing the file with a SQL query to extract data
          from database.
    """

    logger.info('Generating features for the model!')

    with open(sql_path, 'r', encoding='utf-8') as sql_query:
        query = sql_query.read()
        logger.info(f'Going to extract data using the following '
                    f'query:\nSQL file: {sql_path}\nQuery:\n'
                    f'{query}\n')

        try:
            with sqlite3.connect(database_path) as db_conn:
                logger.info(f'Connected to database at '
                            f'{database_path}')
                customer_data = pd.read_sql_query(query,
                                                  db_conn)
                logger.info(f'Sample of data extracted.\n'
                            f'{customer_data.head()}')
                customer_data.to_csv(output_path / csv_path,
                                     index=False)
                logger.info(f'Exported data to {csv_path}')

        except sqlite3.Error as e:
            logger.exception(e)

    logger.success("Features generation complete.")


if __name__ == "__main__":
    app()
