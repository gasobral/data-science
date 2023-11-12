#! /usr/bin/env python3 #
# -*- coding: utf-8 -*- #

import pandas as pd
import numpy  as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

## pandas configuration
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 100)

## matplot configuration
plt.rcParams['figure.figsize'] = (15, 6)
plt.style.use('ggplot')

## importing dataset
elections_data_set = pd.read_csv('../Data Set/clean_data.csv')

## basic dataset information
print(f"Dimensional of imported dataset: {elections_data_set.shape}\n")
print(f"First 5 lines of the dataset\n{elections_data_set.head()}\n")
print(f"Dataset summary\n{elections_data_set.info()}\n")
print(f"Show the number of null data for each column\n"
      f"{elections_data_set.isnull().sum()}\n")

print(f"Showing the number of unique values for each column\n"
      f"{elections_data_set.nunique()}")

## removing column Unnamed: 0 since it is only a record count for
## each line of the dataset
elections_data_set.drop(columns=['Unnamed: 0'], inplace=True)

## analyzing the data for mayors
query_mayors = elections_data_set[
    (elections_data_set['job'] == 'prefeito') &
    (elections_data_set['elector_count'] == 's')
]

## Analyzing the number of mayors elected by main party
mayors_analysis = query_mayors.groupby(by=['main_party']).agg(
    amount=('candidate_vote_count', 'count')
)

number_elected_mayors = mayors_analysis['amount'].sum()
mayors_analysis['%'] = mayors_analysis['amount'] / number_elected_mayors * 100
mayors_analysis['%'] = round(mayors_analysis['%'], 2)
mayors_analysis.sort_values('amount', inplace=True, ascending=False)

## plotting the graphic with the analyzes mayors_analysis
## creating a pallet of colors using seaborn
color_palette = sns.color_palette('magma', len(mayors_analysis))

## configuring the size of the graph
plt.figure(figsize=(20,6))

## plotting the graph itself
plt.bar(mayors_analysis.index,
        mayors_analysis['amount'],
        width=0.9,
        color=color_palette)

## configuring the title
plt.title('Mayors elected in Brazil',
          loc='left',
          fontsize=20,
          color='#404040',
          fontweight=600)

## configuring the labels
plt.ylabel('Amount of mayors')
plt.xlabel('Parties')
plt.xticks(rotation=90)

## changing y axis limit value to add some space after the
## maximum value
plt.ylim(0, mayors_analysis['amount'].max() * 1.1)

## adding labels for each bar of the graph
for position, value in enumerate(mayors_analysis['amount']):
    plt.text(
        ## position of the label
        position -0.3,
        value +10,
        ## label text
        value,
        ## label color
        color=color_palette[position],
        ## label size and font
        size=12,
        fontweight=700
    )

plt.annotate(
    f'Elected in Brazil: {mayors_analysis["amount"].sum()}',
    xy=(0.99,0.94),
    xycoords='axes fraction',
    ha='right',
    va='center',
    color='green',
    fontsize=14,
    bbox=dict(facecolor='#ffffff',
               edgecolor='green',
               boxstyle='round',
               pad=0.25)
)

plt.savefig('mayor_analysis.png')
plt.clf()
plt.close()

## analyzing data for councilors
query_councilors = elections_data_set[
    (elections_data_set['job'] == 'vereador') &
    (elections_data_set['elector_count'] == 's')
]

councilors_analysis = query_councilors.groupby(by='main_party').agg(
    amount = ('candidate_vote_count', 'count')
)

number_elected_councilors = councilors_analysis['amount'].sum()
councilors_analysis['%'] = councilors_analysis['amount'] / number_elected_councilors * 100
councilors_analysis['%'] = round(councilors_analysis['%'], 2)
councilors_analysis.sort_values('amount', inplace=True, ascending=False)

plt.figure(figsize=(12,10))
plt.hlines(
    y=councilors_analysis.index,
    xmin=0,
    xmax=councilors_analysis['amount'],
    lw=5,
    color=color_palette,
    alpha=0.5
)

plt.scatter(
    councilors_analysis['amount'],
    councilors_analysis.index,
    s=100,
    color=color_palette,
    alpha=0.8
)

plt.title('Councilors Elected in Brazil',
          loc='left',
          fontsize=20,
          color='#404040',
          fontweight=500)

plt.annotate(
    f'Elected in Brazil: {councilors_analysis["amount"].sum()}',
    xy=(0.99,0.94),
    xycoords='axes fraction',
    ha='right',
    va='center',
    color='green',
    fontsize=14,
    bbox=dict(facecolor='#ffffff',
               edgecolor='green',
               boxstyle='round',
               pad=0.25)
)

plt.savefig('councilors_analysis.png')
plt.clf()
plt.close()

## correlation analysis
## checking if there is any relationship between the number of mayors
## and councilors elected by party
correlation_table = mayors_analysis['amount'].reset_index()
correlation_table = pd.merge(correlation_table,
                             councilors_analysis.reset_index(),
                             on=['main_party'],
                             how='inner')
correlation_table.columns = ['Party', 'Mayors', 'Councilors', '%']
correlation_table.drop(columns=['%'], inplace=True)

sns.regplot(
    x=correlation_table['Mayors'],
    y=correlation_table['Councilors'],
    ci=95,
    scatter_kws={
        'color': 'blue',
        's': 80,
        'alpha': 0.5},
    line_kws={
        'color': 'orange',
        'alpha': 0.2,
        'lw': 2
    }
)

plt.title('Mayors vs Councilors elected')

## adding the party for mayors and councilors
for line in range(0, correlation_table.shape[0]):
    plt.text(
        correlation_table['Mayors'][line] + 0.8,
        correlation_table['Councilors'][line],
        correlation_table['Party'][line],
        size='medium',
        color='gray',
        weight='semibold'
    )

plt.savefig('correlation_analysis.png')
plt.clf()
plt.close()

## retrieves the amount of candidate by party, elected or not
candidate_party = elections_data_set.groupby(by=['main_party']).count().iloc[:,0:1].reset_index()
candidate_party.columns = ['Party', 'Candidates']

correlation_table = pd.merge(correlation_table,
                             candidate_party,
                             on=['Party'],
                             how='inner')
print(correlation_table.head())

figure = plt.figure(figsize=(15,8))
eixo = figure.add_subplot(111, projection='3d')
eixo.scatter(
    correlation_table['Mayors'],
    correlation_table['Councilors'],
    correlation_table['Candidates'],
    c='black',
    s=100
)

eixo.view_init(30, 185)

eixo.set_xlabel('Mayors')
eixo.set_ylabel('Councilors')
eixo.set_zlabel('Candidates')

# plt.show()
plt.clf()
plt.close()

figura = px.scatter_3d(
    correlation_table,
    x='Mayors',
    y='Councilors',
    z='Candidates',
    color='Party',
    opacity=0.7,
    symbol='Party'
)

figura.show()
