[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/gasobral/data-science/blob/main/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/gasobral/data-science/blob/main/README.pt-br.md)
[![ru](https://img.shields.io/badge/lang-ru-yellow.svg)](https://github.com/gasobral/data-science/blob/main/README.ru.md)

# About the autor
I am a computer scientist with experience in academics and in tech
industry. As support analyst, I worked for two banks companies. My
exprience with data comes from generating reports and indicators of a
regarding a reward system, data migration, lecturing, personal and
freelancer projects. In order to keep developing my data skills, I
read books and create projects.

**Background**: Python | SQL | Machine Learning

**Links**:
- my profile at [Linkedin](https://www.linkedin.com/in/gabriel-sobral-99870846/) and [Kaggle](https://www.kaggle.com/gasobral)
- my [class notes](https://github.com/gasobral/notas-de-aula) about *Data Science* and *programming* in *Python* (only in Brazilian Portuguese)

# Repository Description
A collection of projects created in order to develop data science
skills. I focus in building predictive models using *python*,
*scikit-learn*, *pandas* and *numpy*. However, I also included (in
some projects) graph and dashboard creation using data visualization
tools, since they are important data skills. The area of knowledge of
the projects are bit diverse, allowing us to develop broad view of
data. Below you can find a list of projects followed by their
description.

# Freelance Projects
For some projects I cannot provide much information, due to freelance
contract.

## Forecast Catalogue Price
The catalogue price plays an important role when contracting a
musician, buying or acquiring musical rights. For this reason, I am
working with MZIC to develop a model to predict catalogue price, given
its revenue historical prices. In literature, regression forests
results in accurate models to predict song popularity, we did not
find much about predicting its price. Then we followed a similar
procedure to forecast catalogue price.

# Personal Projects
## [Brazilian Elections](https://github.com/gasobral/data-science/tree/main/brazilian_elections)
Since election is an important topic, I decided to describe Brazilian
election data from 2022. I obtained this data from Electoral Supreme
Court and applied an exploratory data analysis to them. Univariate and
multivariate analysis were done to investigate a relation between
candidate votes, jobs (mayors and councilors only), state and other
variables. By performing this exploratory data analysis I could
provide some interesting data insights. For example, the job and state
has a great influence in total candidate votes, however, in average,
the job has much more influence than the state. Moreover, I showed a
positive the correlation between the number of councilors and mayors
elected.

## [Customer Segmentation](https://github.com/gasobral/data-science/tree/main/client_segmentation)
Identify groups of similars customeres, customer segmentation, is an
important tool for data driven decision at a company for marketing and
product evaluation. Using [Olist data
set](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), we
applied a hierarchical clustering algorithm to identify similar groups
of customers based on customer location (city and state), price, product
category and payment data. Due to computational resources limitation, we
used only 20% of original data do perform a customer segmentation. We
found two groups of customers which are alike in payment type, product
category, price, freight value and payment installments. Most of
customers use credit card, buy items with small value and the preferred
categories are: bed & bath & table, health & beauty, sport, furniture &
decor and informatics. About payment installment, customers usually use
one. But some installment payment range from 2 to 6 because some
e-commerce offers tax free up to 6 installments. However, they differ at
customer location and payment sequential (number of payment
methods). One group of customer uses only one payment method, while the
other group uses two. These information can be useful to describe
customer behavior and to suggest campaigns for most popular
categories. You can find a [presentation](https://github.com/gasobral/data-science/blob/main/client_segmentation/reports/customer_segmentation_presentation.pptx) with the results at report
directory.
