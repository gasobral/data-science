# Client Segmentation

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

## Introduction
Customer segmentation, identify groups of similar customers based on
their characteristics, is an important tool for marketing, making new
products and guiding firm decision [^1] [^2], specially in
e-commerce. In data science, clustering algorithms have been applied
to perform customer segmentation [^1]. Given [Olist
dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
of Brazilian e-commerce, we applied a hierarchical clustering
algorithm to identify similar groups of customers based on customer
location (city and state), price, product category and payment
data. Due to computational resources limitation, we used only 20% of
original data do perform a customer segmentation We found two groups
of customers which are alike in payment type, product category, price,
freight value and payment installments. Most of customers use credit
card, buy items with small value and the preferred categories are: bed
& bath & table, health & beauty, sport, furniture & decor and
informatics. About payment installment, customers usually use one. But
some installment payment range from 2 to 6 because some e-commerce
offers tax free up to 6 installments. However, they differ at customer
location and payment sequential (number of payment methods). One group
of customer uses only one payment method, while the other group uses
two. These information can be useful to describe customer behavior and
to suggest campaigns for most popular categories. You can find a
presentation with the results at report category. Technical details
can be found at notebooks category. Below you will find project
organization and how to execute the code.

[^1]: [Alves Gomes, M., Meisen, T. A review on customer segmentation
    methods for personalized customer targeting in e-commerce use
    cases. Inf Syst E-Bus Manage 21, 527–570
    (2023).](https://doi.org/10.1007/s10257-023-00640-4)

[^2]: [Cooil, B., Aksoy, L., & Keiningham, T. L. (2008). Approaches to
    Customer Segmentation. Journal of Relationship Marketing, 6(3–4),
    9–39.](https://doi.org/10.1300/J366v06n03_02)


## Project Organization

```
├── LICENSE            <- GNU GENERAL PUBLIC LICENSE
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         client_segmentation and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
|
├── sql                <- SQL files
│
└── client_segmentation   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes client_segmentation a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

## How to execute the code

The project has a [makefile](Makefile) to perform the whole process,
that is, obtain the data, train the model and plot the graphs. This can
be done by executing *make all*. If you need to execute a specific step,
below the entire process is broken down:

- *make data* executes [dataset.py](client_segmentation/dataset.py),
which downloads the data set from Kaggle and prepare the data for
training.

- *make features* executes the script
[features.py](client_segmentation/modeling/features.py), it will extract
the required data for the training from data set.

- *make train* trains the model using the
[train.py](client_segmentation/modeling/train.py).

- the plots can be generated by executing *make plots*, it will execute
the [plots.py](client_segmentation/plots.py). The figures can be found
at [figures](reports/figures) directory.
