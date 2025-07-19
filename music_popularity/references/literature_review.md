# Literature review

In this notebook we elaborated a not so comprehensive literature review
about *Hit Song Science problem* using data from streaming services.


## 1. Introduction to Hit Song Science (HSS)

The field of Hit Song Science (HSS) aims to predict the commercial
success of songs by analyzing measurable features, such as audio
characteristics or listener behavior. This area has received increasing
attention due to its economic potential to assist artists, record
labels, and streaming platforms in identifying songs likely to become
hits before release.


## 2. Audio Feature-Based Prediction

Most early studies in HSS focused primarily on intrinsic audio features,
using data available through services like the Spotify Web
API. Middlebrook & Sheik (2019)[^3] developed a model using a dataset of
approximately 1.8 million tracks, combining Spotify audio features with
Billboard chart positions. Their best model, a Random Forest classifier,
achieved an accuracy of 88% in predicting Billboard chart success.

Saragih (2023)[^5] investigated the Indonesian music streaming market
using both regression and classification models. Audio features such as
danceability, acousticness, and energy were assessed for their
predictive value. The study identified Extra Tree Regressor and Random
Forest as the most effective algorithms, and contextualized the results
through Consumer Culture Theory (CCT).

Adeagbo (2020)[^1] conducted the first HSS study focused on the
Afrobeats genre, using a dataset of over 2,000 songs. A classification
model was trained using Spotify features, achieving F1-scores of
approximately 86%. A custom popularity threshold was defined using
Spotify's internal popularity metric.

Gao (2021)[^2] emphasized interpretability by applying SHAP values to
various machine learning models (e.g., random forest, boosting
trees). This study argued that while social media plays a role, audio
features remain the most controllable factor in music production and
thus central to predictive modeling.


## 3. Multimodal Approaches: Integrating Social Media Data

A major contribution in recent literature is the integration of external
variables, particularly from social media platforms. Yee & Raheem
(2022)[^7] were the first to combine YouTube-based social metrics (e.g.,
views, likes, comments) with Spotify audio features. Using a multiclass
classification framework and five different popularity metrics (Length,
Max, Sum, Mean, Debut), their models showed performance gains of 10% to
60% when including YouTube data. Random Forest reached an overall
accuracy of 79.6% .


## 4. User Behavior and Preference Modeling

Some recent studies shifted their focus toward Spotify user behavior,
aiming to reveal how listening patterns and preferences influence
popularity. Shu (2024)[^6] analyzed music trends over time by
correlating features like energy, valence, BPM, and danceability with
user listening habits. Using decision tree and random forest models, the
study found that songs with high energy and valence are more likely to
become popular. The study emphasized the importance of behavioral
analytics for refining recommendation systems and anticipating trends.


## 5. Neural Networks and State-of-the-Art Models

While most studies employed classical models such as decision trees and
random forests, some researchers have explored neural networks to model
more complex patterns. Rusconi (2024)[^4] compared the performance of
Random Forest, SVM, and a Neural Network model on a dataset of 160,000
songs. The neural network performed similarly to the other models,
particularly excelling in identifying "non-hits." The study contributes
to the field by incorporating deep learning into HSS for the first time
using this dataset.


## 6. Summary of Findings

Audio features (danceability, energy, valence, acousticness) remain core
predictors across all studies. Social media signals, particularly from
YouTube, significantly improve predictive performance. Cultural and
regional contexts (e.g., Indonesia, Afrobeats) influence which features
are most predictive. A shift toward interpretable and complex models
(e.g., SHAP, neural networks) marks a new phase in HSS research.


# Bibliography
[^1]: [Adewale Adeagbo. Predicting Afrobeats Hit Songs Using Spotify
    Data. arXiv, 2020](https://doi.org/10.48550/arXiv.2007.03137)

[^2]: [Andrea Gao. Catching the Earworm: Understanding Streaming Music Popularity
      Using Machine Learning Models. E3S Web of Conferences, Volume 253,
      1-16, 2021.](https://doi.org/10.1051/e3sconf/202125303024)

[^3]: [Kai Middlebrook, Kian Sheik. Song Hit Prediction : Predicting
      Billboard Hits Using Spotify Data. arXiv,
      2019.](https://doi.org/10.48550/arXiv.1908.08609)

[^4]: [Giacomo Rusconi. Predicting the Popularity of Spotify Songs Using
      a Neural Network. Tilburg University,
      2024.](https://arno.uvt.nl/show.cgi?fid=171864)

[^5]: [Harriman Samuel Saragih. Predicting song popularity based on
Spotify’s audio features: insights from the Indonesian streaming
users. Journal of Management Analytics, 1-18,
2023.](https://doi.org/10.1080/23270012.2023.2239824)

[^6]: [Miaomiao Shu. Exploring Spotify's Music Popularity Dynamics and
    Forecasting with Machine Learning. Proceedings of the 2nd
    International Conference  on  Applied  Physics  and  Mathematical
    Modeling, 53, 83-89.](https://doi.org/10.54254/2753-8818/53/20240147)

[^7]: [Yap Kah Yee1, Mafas Raheem. Predicting Music Popularity Using
    Spotify and YouTube Features. Indian Journal of Science and
    Technology, 2022, 1786-1799.](https://doi.org/10.17485/IJST/v15i36.2332)
