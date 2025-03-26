from pathlib import Path
from loguru import logger

## setting up project directory structure
## retrive project root
PROJ_ROOT = Path(__file__).resolve().parents[1]
logger.info(f'Project root directory: {PROJ_ROOT}')

## set up data directory structure
DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

## set up reports directory structure
REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

try:
    from tqdm import tqdm

    ## remove a previous log handler
    logger.remove(0)

    ## set tqdm.write to handle log writting when using loguru
    logger.add(lambda msg: tqdm.write(msg, end=''), colorize=True)

except ModuleNotFoundError:
    pass
