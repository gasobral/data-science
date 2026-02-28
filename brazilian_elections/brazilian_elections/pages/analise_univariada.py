## python builtin modules
from pathlib import Path

## python 3rd party modules
from loguru import logger
import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Univariate Analysis")

if st.session_state["dataset"] is not None:
    processed_data = st.session_state["dataset"]
    st.markdown("We start our analysis by checking the numerical data "
                "by providing basic statistics about its central "
                "tendency and dispersion.")
    st.dataframe(processed_data.describe().T)
