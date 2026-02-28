from pathlib import Path

import streamlit as st
import yaml

import config as cfg


## Functions - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
def load_configs(config_file_path: Path) -> dict:
    """
Loads steamlit app configuration from configuration file.

Arguments
---------
    config_file_path: a Path object pointing to a configuration file.

Returns
-------
    A dictionary with the loaded configuration.
    """

    with open(config_file_path, 'r') as config_file:
        configs = yaml.safe_load(config_file)

    return configs


def set_page_config(configs: dict):
    """
Set up page configuration.

Arguments
---------
    configs: a dictionary with streamlit app configuration.
    """

    st.set_page_config(page_title=configs['page']['title'],
                       layout=configs['page']['layout'])


def create_side_bar(configs) -> str:
    """
Creates the menu bar for navigation.

Arguments
---------
    configs: a dictionary with streamlit app configuration.

Returns
-------
    A radio button.
    """

    st.sidebar.title(configs['page']['sidebar']['title'])
    radio_config = configs['page']['sidebar']['radio']
    radio_button = st.sidebar.radio(radio_config['label'],
                                    radio_config['options'])
    return radio_button


def display_home_page(configs):
    """
Display home page contents.

Arguments
---------
    configs: a dictionary with streamlit app configuration.
    """

    st.title(configs['page']['home']['title'])
    st.write(configs['page']['home']['text'])
    st.info(configs['page']['home']['info'])


def display_exploratory_analysis(configs):
    """
Display data exploratory analysis for Olist data set.
    """

    st.title(configs['page']['data']['title'])


## Script - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
## loads the configuration for streamlit app
configs = load_configs(cfg.ST_CONFIG_FILE)

## set up streamlit basic page layout
set_page_config(configs)
radio_button = create_side_bar(configs)

## logic for generating page content
if radio_button == "Home":
    display_home_page(configs)

elif radio_button == "Exploração":
    display_exploratory_analysis(configs)
