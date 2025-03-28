[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/gasobral/data-science/blob/main/brazilian_elections/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/gasobral/data-science/blob/main/brazilian_elections/README.pt-br.md)
[![ru](https://img.shields.io/badge/lang-ru-yellow.svg)](https://github.com/gasobral/data-science/blob/main/brazilian_elections/README.ru.md)

# Eleições brasileiras
## Introdução

Como a eleição é um tópico importante, então decidi descrever os dados
das eleições brasileiras de 2022[^1], onde foram eleitos apenas
prefeitos e vereadores. Obtive esses dados do Supremo Tribunal
Eleitoral e apliquei uma análise exploratória dos dados
neles. Análises univariadas e multivariadas foram realizadas para
investigar a relação entre os votos dos candidatos, cargos (vereador e
prefeito), estado e outras variáveis. Ao performar essa análise
exploratória dos dados, pode prover alguns resultados
interessantes. Por exemplo, o cargo e o estado tem uma grande
influência no total de votos dos candidatos, porém, em média, o cargo
tem uma influência maior do que o estado. Além disso, mostrei uma
correlação positiva entre o número de vereadores e prefeitos eleitos,
separado por partido. Abaixo você encontre os requerimentos do projeto
e como usá-lo.

[^1]: Última data disponível dos dados quando esse projeto fo feito.

## Estrutura do diretório do projeto
```
├── brazilian_elections   <- Código fonte usado no projeto
│   ├── config.py         <- Contém as configurações do projeto
│   ├── dataset.py        <- Script que gera os dados para a análise
│   ├── __init__.py       <- Indica ao python que brazilian_elections é um módulo
│   └── __pycache__
│       ├── config.cpython-310.pyc
│       ├── dataset.cpython-310.pyc
│       └── __init__.cpython-310.pyc
├── data
│   ├── processed         <- Dados depois do processamento
│   └── raw               <- Dados originais
├── LICENSE               <- Licença Open-source
├── Makefile
├── notebooks             <- Jupyter notebook com a análise dos dados
│   └── data_analysis.ipynb
├── pyproject.toml        <- Configuração do projeto e metadados
├── README.md
├── reports               <- Análises geradas (arquivo do Power BI e do Tableau)
│   ├── data_set_source.txt
│   ├── election analysis.pbix
│   ├── election_analysis.twbx
│   └── figures           <- Figuras geradas na análise dos dados
│       ├── correlation_analysis.png
│       ├── correlation_mayors_councilors.png
│       ├── councilors_analysis.png
│       └── mayor_analysis.png
└── requirements.txt
```

## Requerimentos
Este projeto requer módulos normalmente utilizados em ciência dos
dados, que são:

- *pandas*
- *numpy*
- *seaborn*
- *matplotlib*

Para ver os dashboards, criados nesse projeto, você pode usar o
*Tableau*, *Power BI* ou clicar no
[link](https://public.tableau.com/views/election_analysis_17428265010000/Votebashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
para acessar o dashboard no *public Tableau*.


## Como usar
Apenas abre o [notebook de análise de
dados](notebooks/data_analysis.ipynb), no diretório notebooks, e
execute todas as células. Isso irá gerar todas as análises junto com
os gráficos. Note que esse execução irá executar o script
[dataset.py](brazilian_elections/dataset.py) para descompactar os
dados, gerando um arquivo com 80Mb. Os gráficos são plotados no
notebook e também no diretório [figures](reports/figures) (dentro de
reports). Além disso, no diretório [reports](reports), você pode
encontrar os arquivo do *Tableau* e *Power BI* que contêm os
dashboards.
