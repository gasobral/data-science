## python builtin modules
from pathlib import Path

## python 3rd party modules
from loguru import logger
import streamlit as st
import pandas as pd
import plotly.express as px

## user definided modules
from config import PROCESSED_DATA_DIR
import dataset as dt


## Functions - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def retrieve_processed_files(processed_dir: Path) -> list:
    """
Returns a filest with all csv files at processed directory.

Arguments
---------
processed_dir: Path object which points to processed directory.

Returns
-------
A list with all csv processed files.
    """
    return [csv_file for csv_file in processed_dir.glob("*.pqt")]


@st.cache_data
def get_processed_data(file_path: Path) -> pd.DataFrame:
    """
Returns a data frame with the processed data read from a csv file.

Arguments
---------
file_path: Path object containg a path to csv file.

Returns
-------
A data frame with the data read from a csv file.
    """

    processed_data = pd.read_parquet(file_path)
    return processed_data


## Script - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
## loads the data from processed files
processed_files = retrieve_processed_files(PROCESSED_DATA_DIR)

## if a file was found, then generate the data for the plots
if len(processed_files) != 0:
    processed_data = get_processed_data(processed_files[0])
    st.session_state["dataset"] = processed_data

else:
    st.session_date["dataset"] = None

## buils steamlit app page
st.set_page_config(page_title="Brazilian elections analysis",
                   layout="wide")

menu = st.navigation([
    st.Page("pages/home.py",
            title="Home"),
    st.Page("pages/analise_univariada.py",
            title="Univariate analysis"),
    st.Page("pages/analise_multivariada.py",
            title="Multivariate analysis")
])

menu.run()
