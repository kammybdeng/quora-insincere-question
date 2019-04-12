# Quora Insincere Questions Classification Kaggle Challenge

![wordcloud](https://github.com/kammybdeng/quora-insincere-question/blob/master/img/quora_wordcloud.png)

## Contents
- [Introduction](#Introduction)
- [EDA and text cleaning](#EDA)
- [Model](#Model)
- [Outcome](#Outcome)
- [Reference](#Reference)


## Introduction

This challenge is hosted by Kaggle. The objective of this project is to predict whether a question asked on Quora is sincere or not.
https://www.kaggle.com/c/quora-insincere-questions-classification/overview

### What's Quora?
Quora is a platform that empowers people to learn from each other. On Quora, people can ask questions and connect with others who contribute unique insights and quality answers.

### What's an insincere question?
As defined in the [challenge description](https://www.kaggle.com/c/quora-insincere-questions-classification/data), an insincere question is defined as a question intended to make a statement rather than look for helpful answers. Some characteristics are:

- Has a non-neutral tone
- Is disparaging or inflammatory
- Isn't grounded in reality
- Uses sexual content

### What's the evaluation metric?
The metric used for evaluation is [F1 score](https://en.wikipedia.org/wiki/F1_score)

### Word embeddings
Word embeddings are provided and allowed in the challenge.
- [GoogleNews-vectors-negative300](https://code.google.com/archive/p/word2vec/)
- [glove.840B.300d](https://nlp.stanford.edu/projects/glove/)
- [paragram_300_sl999](https://cogcomp.org/page/resource_view/106)
- [wiki-news-300d-1M](https://fasttext.cc/docs/en/english-vectors.html)

## EDA

![EDA](https://github.com/kammybdeng/quora-insincere-question/blob/master/img/targetcount.png)
Imbalanced class


## Text cleaning
After getting a better sense of the data, we want to take create an embedding matrix can be be later used in our models. The challenge is to match words in the training set with the words in the embedding documents. In order to do this, we first need to clean up the text in the training data. The process can be found in my [eda kernel](https://github.com/kammybdeng/quora-insincere-question/blob/master/model/quora-insincere-eda-preprocessing.ipynb).



## Model
To begin, I started with a basic naive bayes model with logistic regression to predict the binary labels. Later, I learned about the LSTM model and tried to add in new layers to boost up the result.

  0. Naive Bayes with Logistic Regression Model baseline [link to model_0](https://github.com/kammybdeng/quora-insincere-question/blob/master/model/model_0.ipynb)
  1. LSTM Neural Network with basic text cleanings and no embeddings weights [link to model_1](https://github.com/kammybdeng/quora-insincere-question/blob/master/model/model_1.ipynb)
  2. LSTM and GRU Neural Network with embeddings weights (GloVe) [link to model_2](https://github.com/kammybdeng/quora-insincere-question/blob/master/model/model_2.ipynb)
  3. Trained with KFold
  4. LSTM and GRU Neural Network with embeddings weights and adjusted parameters(GloVe)[link to model_3](xxx)

## What are RNN and LSTM?

It's my first time implementing neural network model. I ran into a lot of difficulties and spent a great amount of time to learn the concepts while I was training the models. **I have compiled a [notebook](https://github.com/kammybdeng/quora-insincere-question/blob/master/nn_notes.md) to record my understand of the topic.**

## Outcome

| Model         | Public Score  | Rank  |
| ------------- |:-------------:| -----:|
| model 0       | 0.64283       | xxxx  |
| model 1       | 0.65081       | xxxx  |
| model 2       | 0.67055       | xxxx  |
| model 3       | 0.6xxxx       | xxxx  |
| model 4       | 0.6xxxx       | xxxx  |

**Note: These are all late submission, hence they are not shown on the public leaderboard**

## Reference

- https://www.kaggle.com/ashishpatel26/nlp-text-analytics-solution-quora
- https://www.kaggle.com/christofhenkel/how-to-preprocessing-when-using-embeddings
