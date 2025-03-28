[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/gasobral/data-science/blob/main/brazilian_elections/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/gasobral/data-science/blob/main/brazilian_elections/README.pt-br.md)
[![ru](https://img.shields.io/badge/lang-ru-yellow.svg)](https://github.com/gasobral/data-science/blob/main/brazilian_elections/README.ru.md)

# Brazilian Elections
## Introduction

Since election is an important topic, I decided to describe Brazilian
election data from 2022[^1], only for mayors and councilors. I
obtained this data from Superior Electoral Court and applied an
exploratory data analysis to it. Univariate and multivariate analysis
were done to investigate a relation between candidate votes, jobs
(mayors and councilors), state and other variables. By performing this
exploratory data analysis, I could provide some interesting data
insights. For example, the job and state have a great influence in
total candidate votes, however, in average, the job has much more
influence than the state. Moreover, I showed a positive the
correlation between the number of councilors and mayors elected,
breakdown by party. Below you can find project requirements and how to
use it.

[^1]: Latest data available when this project was done.

## Project directory structure
```
├── brazilian_elections   <- Source code for use in this project.
│   ├── config.py         <- Store useful variables and configuration
│   ├── dataset.py        <- Scripts to download or generate data
│   ├── __init__.py       <- Makes brazilian_elections a Python module
│   ├── plots.py          <- Code to create visualizations
│   └── __pycache__
│       ├── config.cpython-310.pyc
│       ├── dataset.cpython-310.pyc
│       └── __init__.cpython-310.pyc
├── data
│   ├── processed         <- Data after being processed
│   └── raw               <- The original, immutable data dump.
├── LICENSE               <- Open-source license
├── Makefile
├── notebooks             <- Jupyter notebook with data analysis
│   └── data_analysis.ipynb
├── pyproject.toml        <- Project configuration file with package metadata for
├── README.md
├── reports               <- Generated analysis (Power BI and Tableau files)
│   ├── data_set_source.txt
│   ├── election analysis.pbix
│   ├── election_analysis.twbx
│   └── figures           <- Generated graphics and figures to be used in reporting
│       ├── correlation_analysis.png
│       ├── correlation_mayors_councilors.png
│       ├── councilors_analysis.png
│       └── mayor_analysis.png
└── requirements.txt
```

## Requirements
This project requires modules that are usually used in data science, which
are:

- *pandas*
- *numpy*
- *seaborn*
- *matplotlib*

In order to view the dashboards created in this project, you can use
*Tableau*, *Power BI* or click on the following
[link](https://public.tableau.com/views/election_analysis_17428265010000/Votebashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
to access the dashboard in *public Tableau*.

## How to use it
Just open the [data analysis notebook](notebooks/data_analysis.ipynb),
in notebooks directory, and execute all its cells. This will generate
all the analysis along side with the graphs. Note that this execution
will call the script [dataset.py](brazilian_elections/dataset.py)
in order to decompress the data, which will create a file with
80Mb. The graphs are plotted in the notebook and also in
[figures](reports/figures) directory (under reports). And also, in
[reports](reports) directory you can find the files which contain
*Tableau* and *Power BI* dashboards.
