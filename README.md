# Quora Insincere Questions Classification Kaggle Challenge
![wordcloud](https://github.com/kammybdeng/quora-insincere-question/blob/master/img/quora_wordcloud.png)
## Contents
- [Introduction](#Introduction)
- [EDA and text cleaning](#EDA)
- [Model](#Model)
- [Outcome](#Outcome)
- [Reference](#Reference)


## Introduction

This challenge is hosted by Kaggle. The objective is to **predict whether a question asked on Quora is sincere or not.**
https://www.kaggle.com/c/quora-insincere-questions-classification/overview

### What's Quora?
Quora is a platform that empowers people to learn from each other. On Quora, people can ask questions and connect with others who contribute unique insights and quality answers.

### What's an insincere question?
As defined in the [challenge description](https://www.kaggle.com/c/quora-insincere-questions-classification/data), an insincere question is a question intended to make a statement rather than look for helpful answers. Some characteristics are:

- Has a non-neutral tone
- Is disparaging or inflammatory
- Isn't grounded in reality
- Uses sexual content

The metric used for evaluation is [F1 score](https://en.wikipedia.org/wiki/F1_score), and word embeddings are provided and allowed in this challenge.
- [GoogleNews-vectors-negative300](https://code.google.com/archive/p/word2vec/)
- [glove.840B.300d](https://nlp.stanford.edu/projects/glove/)
- [paragram_300_sl999](https://cogcomp.org/page/resource_view/106)
- [wiki-news-300d-1M](https://fasttext.cc/docs/en/english-vectors.html)

## EDA

![EDA](https://github.com/kammybdeng/quora-insincere-question/blob/master/img/targetcount.png)
The dataset is an imbalanced class with 94% sincere questions and only 6% insincere questions. Thus, the F1 score is a great metric for model evaluation in this case.


## Text cleaning
After getting a better sense of the data, we want to take create an embedding matrix can be used in our models. The challenge is to match words in the training set with the words in the embedding documents. In order to do this, we first need to clean up the text in the training data. The process can be found in my [eda kernel](https://github.com/kammybdeng/quora-insincere-question/blob/master/model/quora-insincere-eda-preprocessing.ipynb) along with additional functions in [here](xxx).



## Model
To begin, I started with a basic naive bayes model with logistic regression to predict the binary labels. Later, I learned about the LSTM model and tried to add in new layers to boost up the result.

  0. **Naive Bayes with Logistic Regression** Model baseline [link to model_0](https://github.com/kammybdeng/quora-insincere-question/blob/master/model/model_0.ipynb)
  1. **LSTM** Neural Network with basic text cleanings and **no embeddings weights** [link to model_1](https://github.com/kammybdeng/quora-insincere-question/blob/master/model/model_1.ipynb)
  2. **LSTM and GRU** Neural Network with **embeddings weights** (GloVe) [link to model_2](https://github.com/kammybdeng/quora-insincere-question/blob/master/model/model_2.ipynb)
  - 1st layer: embedding layer as pretrained weights
  - 2nd layer: spatial dropout
  - 3rd layer: bidirectional with LSTM
  - 4th layer: bidirectional with GRU
  - 5th layer: global max pooling 1D
  - 6th layer: 2 dense layers (size 16 and 32)
  - 7th layer: output dense layers
  3. Trained with **KFold** [link to model_3](https://github.com/kammybdeng/quora-insincere-question/blob/master/model/model_3.ipynb)
  4. **LSTM and GRU** Neural Network with **embeddings weights** and **adjusted parameters**(GloVe)[link to model_4](xxhttps://github.com/kammybdeng/quora-insincere-question/blob/master/model/model_4.ipynbx)
  - 1st layer: embedding layer as pretrained weights
  - 2nd layer: spatial dropout
  - 3rd layer: bidirectional with LSTM
  - 4th layer: bidirectional with GRU
  - 5th layer: 2 global max pooling 1D
  - 6th layer: output dense layer

## What are RNN and LSTM?

Since it's my first Kaggle challenge and also the first time to implement neural network models, I ran into a lot of difficulties and spent a great amount of time to learn the concepts while I was doing the challenge. **I have compiled a [notebook](https://github.com/kammybdeng/quora-insincere-question/blob/master/nn_notes.md) to record my notes and understanding of the topic.**

## Outcome

| Model         | Public Score  | Rank  |
| ------------- |:-------------:| -----:|
| model 0       | 0.64283       | 1271/4037 (top 32%)  |
| model 1       | 0.65081       | 1252/4037 (top 31%)  |
| model 2       | 0.67055       | 1205/4037 (top 30%)  |
| model 3       | 0.68037       | 1149/4037 (top 29%)  |
| model 4       | 0.6xxxx       | xxxx  |

**Note: These are all late submissions, hence they are not shown on the public leaderboard**

Though my scores are as not astonishing as most Kagglers', I had gained so, so much more knowledge of Word Embeddings and Neutral Network from where I was months ago. The entire process took around three weeks on learning about the new concepts, working on Kaggle, and writing up this repository. I'm proud to say that this is a milestone in my Data Science journey. There are still a lot of skills and concepts that I need to learn and improve. Yet, I'm excited for the challenges ahead and would love to share and discuss with other colleagues who also share the same passion in Data Science or Machine Learning. You are very welcome to contact me if you have any comments or feedback!

## Reference

This project would not made possible without the help from the supportive Kaggle community. Below are the Kagglers that have provided great insights and codes for the challenge.

- https://www.kaggle.com/ashishpatel26/nlp-text-analytics-solution-quora
- https://www.kaggle.com/christofhenkel/how-to-preprocessing-when-using-embeddings
- https://www.kaggle.com/ryanzhang/tfidf-naivebayes-logreg-baseline
- https://www.kaggle.com/shujian/single-rnn-with-4-folds-clr
- https://www.kaggle.com/sudalairajkumar/a-look-at-different-embeddings
- https://www.kaggle.com/wowfattie/3rd-place
- https://www.kaggle.com/christofhenkel/how-to-preprocessing-when-using-embeddings
