# Soft intro to Neural Network

- [Conventional Neural Network](#Conventional-Neural-Network)
- [Recurrent Neural Network](#Recurrent-Neural-Network)
- [LSTM](#LSTM)
- [GRU](#GRU)
- [Bidirectional](#Bidirectional)
- [Reference](#Reference)

## Conventional Neural Network
![conventionalnn](https://github.com/kammybdeng/quora-insincere-question/blob/master/img/convolutional_neural_network.png)

### Sample layers

1. **Input Layer**

2. **Convolution**              | →  produce feature maps that preserve spatial relationships in data

3. **Pooling/Subsampling**    	| →  reduce data dimensionality and the number of parameters

4. **Flatten**			            |	→  flatten the matrix to a desirable size

5. **Activation** 	           	|	→  transform outputs to non-linear relationship, e.g. sigmoid can restrain results to [0,1] and ReLU can restrain results to [0, +]

## Recurrent Neural Network
![rnn_vs_rrnn](https://github.com/kammybdeng/quora-insincere-question/blob/master/img/rnn_vs_rrnn.png)

### How is RNN different from CNN?

RNN learns from previous events, where CNN does not. Quoted from one of the resources, “RNN works on the principle of saving the output of a layer and feeding this back to the input in order to predict the output of the layer.”

| Conventional Neural Network            | Recurrent Neural Network
| ---------------------------------      |:-------------------------
| feed-forward                           | feedback/recurrent
| recognize pattern across **space**     | recognize pattern across **time**
| fixed size input and output            | arbitrary input and output
| ideal for images and videos            | ideal for text and speech      


### Sample layers

1. **Input Layer**

2. **Embedding layer**   →  assign pretrained weights to model

3. **Bidirectional**     →  train from both directions X(t) -> X(t+1) and X(t+1) -> X(t)

4. **Dense**             → shrink the matrix/data to a smaller size

5. **Dropout** 		  	   → prevent overfitting, large dimension layer could have higher dropout rate

However, sometimes the previous events are not very helpful for us or the machine to understand the big picture. Therefore, another branch of RNN is created and it’s called **LSTM (Long Short Term Memory)**

## LSTM
![lstm](https://github.com/kammybdeng/quora-insincere-question/blob/master/img/lstm_model.png)

LSTMs, Long Short Term Memory networks, are a special kind of RNN that are capable of learning long-term dependencies. They can remember information for long periods of time., where as standard RNNs struggles to learn. The sophisticated design of the LSTMs allows them to forget and keep previous information in a more precise way.

## GRU
To determine how much of the past information needs to be passed to the output or to forget, GRUs, Gated Recurrent Unit, are models that update and reset the gates.

## Bidirectional
Use both past and future information to get a better sense of current input.


**Forward direction** - will learn the past

**Backward direction** - will learn the future (because it starts from the end and learns backward)

#### Example:
**Goal**: Is **Teddy** a name or not?
  - He said, "Teddy bears are on sale!"
  - He said, "Teddy Roosevelt was a great President!"

By using the bidirectional technique, we can capture both the information before **("said")** and after **("bears"/"Roosevelt")** the word **"Teddy"**.


## Reference

This project would not made possible without the great resources from the Data Science community. Below are all the references that I used when compiling this notebook. All of them provided great explanation and examples of the topic.

- https://hackernoon.com/understanding-architecture-of-lstm-cell-from-scratch-with-code-8da40f0b71f4
- http://blog.echen.me/2017/05/30/exploring-lstms/
- https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/
- https://www.youtube.com/watch?v=bTXGpATdKRY
- https://machinelearningmastery.com/when-to-use-mlp-cnn-and-rnn-neural-networks/
- https://www.quora.com/What-is-the-difference-between-CNN-and-RNN
- https://medium.freecodecamp.org/an-intuitive-guide-to-convolutional-neural-networks-260c2de0a050
- https://towardsdatascience.com/recurrent-neural-networks-and-lstm-4b601dd822a5
