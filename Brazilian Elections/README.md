# Brazilian Elections

## Introduction

Since election is an important topic, I decided to describe Brazilian
election data from 2022[^1], which elected only mayors and
councilors. I obtained this data from Electoral Supreme Court and
applied an exploratory data analysis to it. Univariate and
multivariate analysis were done to investigate a relation between
candidate votes, jobs (mayors and councilors), state and other
variables. By performing this exploratory data analysis, I could
provide some interesting data insights. For example, the job and state
has a great influence in total candidate votes, however, in average,
the job has much more influence than the state. Moreover, I showed a
positive the correlation between the number of councilors and mayors
elected, breakdown by party. Below you can find project requirements
and how to use it.

[^1]: Latest data available when this project was done.

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
Just execute the script data_visualization.py, in Source Code directory,
to generate the graphs of jobs elected by party and the correlation graph
between the number of mayors and councilors elected.

Still in Source Code directory, you can find the notebook
data_analysis.ipynb, which has the data exploratory analysis.
