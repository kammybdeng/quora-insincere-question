# Soft intro to Neural Network


## Conventional Neural Network
![conventionalnn](https://github.com/kammybdeng/quora-insincere-question/blob/master/img/convolutional_neural_network.png)

#### Sample layers

1. Input Layer

2. Convolution               →  preserves the spatial relationship

3. Pooling/Subsampling    	 →  reduce the dimensionality

Step 2 and 3 can be repeated for multiple times (optional)

4. Flatten				 →  the matrix to a column vector to feed into MLP

5. Dropout 			 →  to prevent overfitting, higher dropout rate should apply on layer with larger content/dimension/

## Recurrent Neural Network



### How is it different from CNN:

It learns from previous events. Quoted from one of the resources, “After seeing each image, the model outputs a label and also updates the knowledge it's been learning”

However, sometimes the previous events are not very helpful for us or the machine to understand the big picture. Therefore, another branch of RNN is created and it’s called **LSTM (Long Short Term Memory)**

## LTSM
![lstm](https://github.com/kammybdeng/quora-insincere-question/blob/master/img/lstm_model.png)


#### Sample layers

1. Input Layer

2. Embedding layer   →  assign embedding weights

3. Bidirectional →    train from both directions X(t) -> X(t+1) and X(t+1) -> X(t)

3. Attention layer  → telling the model which part that it needs to pay more attention to

4. Dense           → to shrink the matrix/data to a smaller size

5. Dropout 			   →  to prevent overfitting, higher dropout rate should apply on layer with larger content/dimension/



### Bidirectional
use both past and future information to get a better sense of current input.

**Forward direction** - past

**Backward direction** - future

Example:

He said, “Teddy
He said, “Teddy


### Credits:

https://hackernoon.com/understanding-architecture-of-lstm-cell-from-scratch-with-code-8da40f0b71f4

https://developer.nvidia.com/discover/convolutional-neural-network

http://blog.echen.me/2017/05/30/exploring-lstms/

https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/
