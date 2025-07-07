[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/gasobral/data-science/blob/main/brazilian_elections/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/gasobral/data-science/blob/main/brazilian_elections/README.pt-br.md)
[![ru](https://img.shields.io/badge/lang-ru-yellow.svg)](https://github.com/gasobral/data-science/blob/main/brazilian_elections/README.ru.md)

# Выборы в Бразилии
## Введение

Поскольку выборы важная тема, я решил описать данные бразильского
выборов 2022[^1] года, только для мэров и советников. Я извлёк данные
с сайта Высшего Избирательного Суда и применил к ним разведочный
анализ данных. Одномерный и многомерный анализ проведены для изучения
соотношения между голосами кандидатов, должностями (мэры и советники),
штатом и другими переменными. Выполнив этот разведочный анализ данных,
я смог представить некоторые интересные выводы. Например, должность и
штат оказывают большое влияние на общее количество голосов кандидатов,
однако, в среднем, должность оказывает гораздо большее влияние, чем
штат. Более того, я показал положительную корреляцию между числом
избранных советников и мэров, в разбивке по партиям. Ниже вы можете
найти требования к проекту и как его использовать.

[^1]: Последние данные доступны на момент завершения проекта.

## Структура каталогов проекта
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

## Требования
Для этого проекта требуются модули, которые обычно используются в data
science, а именно:

- *pandas*
- *numpy*
- *seaborn*
- *matplotlib*

Для просмотра панелей мониторинга, созданных в этом проекте, вы можете
использовать *Tableau*, *Power BI* или  нажмите на следующую ссылку
[ссылку](https://public.tableau.com/views/election_analysis_17428265010000/Votebashboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link),
чтобы показать панель мониторинга на *public Tableau*.

## Как запустить
Только откройте [блокнот анализа
данных](notebooks/data_analysis.ipynb), внутри каталога notebooks, и
выполите все ячейки. Это создаёт весь анализ вместе с
графиками. Обратите внимание, что это выполнение запустит скрипт
[dataset.py](brazilian_elections/dataset.py) для того, чтобы
распаковать данные и создаёт файл размером 80 Мбайт. Графики строятся
в блокноте, а также в каталоге [figures](reports/figures). Более того,
в каталоге [reports](reports) вы можете найти файлы, которые содержат
*Tableau* и *Power BI* панели мониторинга.
