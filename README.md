# Quora Insincere Questions Classification Kaggle Challenge

![wordcloud](https://github.com/kammybdeng/quora-insincere-question/blob/master/img/quora_wordcloud.png)

# Contents
[Introduction](#Introduction)
[EDA and text cleaning](#EDA)
[Model](#Model)
[Outcome](#Outcome)
[Reference](#Reference)


## Introduction

This challenge is hosted by Kaggle. The objective of this project is to predict whether a question asked on Quora is sincere or not.
https://www.kaggle.com/c/quora-insincere-questions-classification/overview

#### What's Quora?
Quora is a platform that empowers people to learn from each other. On Quora, people can ask questions and connect with others who contribute unique insights and quality answers.

#### What's an insincere question?
As defined in the [challenge description](https://www.kaggle.com/c/quora-insincere-questions-classification/data)

An insincere question is defined as a question intended to make a statement rather than look for helpful answers. Some characteristics are:

- Has a non-neutral tone
- Is disparaging or inflammatory
- Isn't grounded in reality
- Uses sexual content

#### What's the evaluation metric?
The metric used for evaluation is [F1 score](https://en.wikipedia.org/wiki/F1_score)

#### Word embeddings
Word embeddings are provided and allowed in the challenge.
- [GoogleNews-vectors-negative300](https://code.google.com/archive/p/word2vec/)
- [glove.840B.300d](https://nlp.stanford.edu/projects/glove/)
- [paragram_300_sl999](https://cogcomp.org/page/resource_view/106)
- [wiki-news-300d-1M](https://fasttext.cc/docs/en/english-vectors.html)

## EDA

![EDA](https://github.com/kammybdeng/quora-insincere-question/blob/master/img/targetcount.png)
Imbalanced class


## Text cleaning
The biggest challenge. Tried multiple ways to clean the data.



## Model
  0. Naive Bayes with Logistic Regression Model baseline
  1. LSTM Neural Network with no embeddings weights
  2. LSTM and GRU Neural Network with embeddings weights (GloVe)
  3. LSTM and GRU and attention layer Neural Network with embeddings weights (GloVe)


## Outcome

| Model         | Public Score  | Rank  |
| ------------- |:-------------:| -----:|
| model 0       | 0.64283       | xxxx  |
| model 1       | 0.6xxxx       | xxxx  |
| model 2       | 0.6xxxx       | xxxx  |
| model 3       | 0.6xxxx       | xxxx  |

**Note: These are all late submission, hence they are not shown on the public leaderboard**

## Reference

- https://www.kaggle.com/ashishpatel26/nlp-text-analytics-solution-quora
- https://www.kaggle.com/christofhenkel/how-to-preprocessing-when-using-embeddings
