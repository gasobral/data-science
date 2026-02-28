[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/gasobral/data-science/blob/main/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/gasobral/data-science/blob/main/README.pt-br.md)
[![ru](https://img.shields.io/badge/lang-ru-yellow.svg)](https://github.com/gasobral/data-science/blob/main/README.ru.md)

# Sobre o autor
Sou cientista da computação com experiência em modelagem preditiva,
análise exploratória e engenharia de dados. Tenho doutorado em ciência da
computação e atuo na Cielo com clusterização e classificação da maturidade
digital de clientes, utilizando Databricks, SQL, PySpark e
Python. Desenvolvi projetos envolvendo machine learning, séries temporais
e pipelines ELT com DBT e Snowflake. Lecionei disciplinas de programação,
banco de dados e ciência de dados, e mantenho projetos pessoais voltados à
análise e visualização de dados.

**Background**: Python | SQL | Machine Learning

**Links**:
- meu perfil no [Linkedin](https://www.linkedin.com/in/gabriel-sobral-99870846/) e no [Kaggle](https://www.kaggle.com/gasobral)
- minhas [notas de aula](https://github.com/gasobral/notas-de-aula) sobre *Data Science* e *programação* em *Python*

# Descrição do Repositório
Uma coleção de projetos criados para desenvolver habilidades em
ciência dos dados. Foquei em construir modelos preditivos usando
*python*, *scikit-learn*, *pandas* e *numpy*. Porém, também incluí (em
alguns projetos) criação de gráficos e dashboards usando ferramentas
de visualização de dados, pois são habilidades importantes. A área de
conhecimento dos projetos é diversa, permitindo desenvolver uma visão
ampla da área de dados. Abaixo você encontra uma lista dos projetos
junto com a sua descrição.

# Projetos de Freelancer
## Projeção de preço de Catálogos
O preço de catálogos tem um papel importante ao contratar um(a)
músico(a), comprar ou adquirir direitos musicais. Por esse motivo, estou
trabalhando com a MZIC a fim de desenvolver um modelo para predizer o
valor do catálogo, dado o preço histórico de revenda de suas
músicas. Na literatura, florestas de regressão resultam em modelos
precisos para prever a popularidade de músicas, não encontramos muito
sobre a predição de valores. Sendo assim, seguimos uma abordagem similar
para projetarmos o preço do catálogo.

# Projetos Pessoais
## [Eleições Brasileiras](https://github.com/gasobral/data-science/tree/main/brazilian_elections)
Como a eleição é um assunto importante, decidi descrever os dados da
eleição brasileira de 2022. Obtive tais dados do Supremo Tribunal
Eleitoral (TSE) e apliquei uma análise exploratória neles. Foram
realizadas análises univariada e multivariada para investigar a
relação enter votos dos candidatos, cargo (prefeito ou vereador),
estado e outras variáveis. Ao performar essa análise, pude
providenciar resultados interessante. Por exemplo, o cargo e o estado
têm uma grande influência no número total de votos, entretanto, na
média, o carga tem mais influência do que estado. Além disso, pude
mostrar uma correlação positiva entre o número de vereados e prefeitos
eleitos.

## [Segmentação de Clientes](https://github.com/gasobral/data-science/tree/main/client_segmentation)
Identificar grupos de clientes similares, segmentação de clientes, é uma
ferramenta importante para uma tomada de decisão baseada em dados numa
empresa, seja para o marketing ou avaliação de produtos. Usando o [data
set da
Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce),
aplicamos um algoritmo de clusterização hierárquico para identificar
grupos de clientes similares baseado na sua localização (cidade e
estado), preço, categoria do produto e informações sobre o
pagamento. Devido a uma limitação de recursos computacionais, utilizamos
apenas 20% dos dados originais para fazer a segmentação de
clientes. Encontramos dois grupos de clientes, que são similares em
relação ao tipo de pagamento, categoria de produto, preço, valor do
frete e número de parcelamentos. A maioria dos clientes usam cartão de
crédito, compram itens de pequeno valor e suas categorias preferidas
são: cama & mesa & banho, saúde & beleza, esportes, móveis & decoração e
informática. Sobre o número de parcelas, os clientes normalmente fazem
apenas uma. Porém há alguns pagamentos parcelados de 2 a 6 meses, pois
os e-commerces normalmente oferecem parcelamentos sem juros em até 6
vezes. No entanto, eles diferem sobre a localização e no número de meios
de pagamento. Um grupo de clientes usam apenas um meio de pagamento,
enquanto que o outro grupo usa dois. Os resultados encontrados podem ser
úteis para descrever os clientes e sugerir campanhas para as categorias
mais populares. Você pode encontrar uma [apresentação](https://github.com/gasobral/data-science/blob/main/client_segmentation/reports/customer_segmentation_presentation.pptx) destes resultados
no diretório report.
