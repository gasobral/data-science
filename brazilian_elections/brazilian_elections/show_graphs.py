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
    return [csv_file for csv_file in processed_dir.glob("*.csv")]


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

    processed_data = pd.read_csv(file_path)
    return processed_data


def avg_vote_per_job_data(processed_data: pd.DataFrame) -> pd.DataFrame:
    """
Returns a data frame with the votes per state and job.

Arguments
---------
processed_data: a data frame with processed electoral data.

Returns
-------
A data frame with the votes per state and job.
    """

    vote_per_state_job = processed_data.\
        groupby(by=['job', 'uf'])['candidate_vote_count'].mean()
    vote_per_state_job =  vote_per_state_job.reset_index(['job', 'uf'])
    return vote_per_state_job


def sum_vote_per_job_data(processed_data: pd.DataFrame) -> pd.DataFrame:
    """
Returns a data frame with the votes per state and job.

Arguments
---------
processed_data: a data frame with processed electoral data.

Returns
-------
A data frame with the votes per state and job.
    """

    vote_per_state_job = processed_data.\
        groupby(by=['job', 'uf'])['candidate_vote_count'].sum()
    vote_per_state_job =  vote_per_state_job.reset_index(['job', 'uf'])
    return vote_per_state_job


def get_candidate_vote_data(processed_data: pd.DataFrame,
                            state: str,
                            job: str) -> pd.DataFrame:
    """
Given a data frame, returns the candidate votes for a job and state.

Arguments
---------
processed_data: a data frame containg the processed electoral data.
state: a string representing a brazilian state (uf).
job: a string describing the job (mayor or councilor).

Return
------
A data frame for job and state given.
    """

    mask = (processed_data['uf'] == state) & (processed_data['job'] == job)
    candidate_vote = processed_data[mask]
    return candidate_vote['candidate_vote_count']


def get_vote_party(processed_data: pd.DataFrame) -> tuple:
    """
Given electoral processed data, returns two data frames with the sum and
mean of the votes breakdown by party.

Arguments
---------
processed_data: a data frame with processed electoral data.

Returns
-------
A tuple with two data frames with sum and mean of votes breakdown by
party.
    """

    vote_job_party = processed_data.groupby(by=['job', 'main_party'])
    sum_votes = vote_job_party['candidate_vote_count'].sum().\
        reset_index()
    mean_votes = vote_job_party['candidate_vote_count'].mean().\
        reset_index()

    return (sum_votes, mean_votes)


def get_job_elected(processed_data: pd.DataFrame,
                    job: str) -> pd.DataFrame:
    """
    Retreive the number elected candidates per party for a job
    (mayor or councilor).

Arguments
    ---------
    processed_data: a data frame contaning the electoral processed data.
    job: a string representing a job (mayor or councilor).

Returns
    -------
    A data frame with the number of elected candidates per party for a
    given job.
    """

    mask = (processed_data['job'] == job) &\
        (processed_data['elector_count'] == 's')
    elected_candidates = processed_data[mask].copy()
    elected_analysis = elected_candidates.groupby(by=['main_party']).\
        agg(amount=('candidate_vote_count', 'count')).reset_index()

    number_elected = elected_analysis['amount'].sum()
    elected_analysis['%'] = elected_analysis['amount'] /\
        number_elected * 100
    elected_analysis['%'] = round(elected_analysis['%'], 2)
    elected_analysis.sort_values(by='amount',
                                 inplace=True,
                                 ascending=False)

    return elected_analysis


## Script - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
URL_PROJECT = 'https://github.com/gasobral/data-science/tree/main/brazilian_elections'
URL_NOTEBOOK = 'https://github.com/gasobral/data-science/blob/main/brazilian_elections/notebooks/data_analysis.ipynb'

## find all csv files at processed data directory
processed_files = retrieve_processed_files(PROCESSED_DATA_DIR)

## if any csv file were found, then generate the data for the plots
if len(processed_files) != 0:
    processed_data = get_processed_data(processed_files[0])

    st.title("Brazlian electoral data analysis")
    st.markdown(f"In [Brazilian electoral project]({URL_PROJECT}), we"
                f" analised electoral data from 2022 and provided some"
                f" data insights. For in depth discussion, please "
                f" this [notebook]({URL_NOTEBOOK}). Below we provide "
                f" some interative graphs regardings our analysis.")

    ## generates the data for the plots
    ## plot - average candidate votes per job and state
    vote_per_job = avg_vote_per_job_data(processed_data)
    st.subheader("Average of candidate votes per job and state.")
    st.bar_chart(data=vote_per_job,
                 x='uf',
                 y='candidate_vote_count',
                 color='job')

    ## plot - sum of candidate votes per job and state
    vote_per_job = sum_vote_per_job_data(processed_data)
    st.subheader("Sum of candidate votes per job and state.")
    st.bar_chart(data=vote_per_job,
                 x='uf',
                 y='candidate_vote_count',
                 color='job')

#    ## plot - histogram of candidate votes, given job and state
#    st.subheader("Histogram of candidate votes for job and state.")
#    col1, col2 = st.columns(2)
#
#    with col1:
#        jobs = processed_data['job'].unique()
#        job_selection = st.selectbox(
#            "Select a job",
#            options=jobs,
#            index=0
#        )
#
#    with col2:
#        states = processed_data['uf'].unique()
#        state_selection = st.selectbox(
#            "Select a state (uf)",
#            options=states,
#            index=0
#        )
#
#    candidate_vote_histogram = get_candidate_vote_data(processed_data,
#                                                       state_selection,
#                                                       job_selection)
#    fig = px.histogram(candidate_vote_histogram)
#    st.plotly_chart(fig)
#
#
#    ## plot the number of elected mayors and councilors
#    st.subheader("Number of mayors elected")
#    mayor_elected = get_job_elected(processed_data, 'prefeito')
#    st.bar_chart(data=mayor_elected,
#                 x='main_party',
#                 y='amount')
#
#    st.subheader("Number of councilors elected")
#    councilor_elected = get_job_elected(processed_data, 'vereador')
#    st.bar_chart(data=councilor_elected,
#                 x='main_party',
#                 y='amount')
#
#    ## total de votor por partido e job
#    sum_vote_party, total_vote_party = get_vote_party(processed_data)
#    st.subheader("Sum of candidade votes per job and main party.")
#    st.bar_chart(data=sum_vote_party,
#                 x='main_party',
#                 y='candidate_vote_count',
#                 color='job')
#
#    st.subheader("Average of candidade votes per job and main party.")
#    st.bar_chart(data=total_vote_party,
#                 x='main_party',
#                 y='candidate_vote_count',
#                 color='job')
