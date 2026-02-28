import streamlit as st

URL_PROJECT = 'https://github.com/gasobral/data-science/tree/main/brazilian_elections'
URL_NOTEBOOK = 'https://github.com/gasobral/data-science/blob/main/brazilian_elections/notebooks/data_analysis.ipynb'

st.title("Brazlian electoral data analysis from 2022")
st.markdown(
    f"In [Brazilian electoral project]({URL_PROJECT}), we "
    f"did an exploratory data analysis of Brazilian election data from "
    f"2022, retrieved from Superior Electoral Court (TSE, in Brazilian "
    f"Portuguese). We performed univariate and multivariate analysis "
    f"to describe and investigate relationships about vote, party and "
    f"region, which includes a data dictionary as well. We found the "
    f"job, mayor or councilor, plays an important role in the amount of "
    f"votes received. Moreover, we also found a positive correlation "
    f"between the number of mayors an councilors elected by party. "
    f"You can check the analysis made using the navigation menu or "
    f"in this [notebook]({URL_NOTEBOOK})."
)
