# Soft intro to Neural Network


## Conventional Neural Network

#### Steps
Input

Convolution                		 →  preserves the spatial relationship

Pooling/Subsampling   . 	 →  reduce the dimensionality

Step 2 and 3 can be repeated for multiple times (optional)

Flatten				 →  the matrix to a column vector to feed into MLP

Dropout 			 →  to prevent overfitting

## Recurrent Neural Network

### How is it different from CNN:

It learns from previous events. Quoted from one of the resources, “After seeing each image, the model outputs a label and also updates the knowledge it's been learning”

However, sometimes the previous events are not very helpful for us or the machine to understand the big picture. Therefore, another branch of RNN is created and it’s called **LSTM (Long Short Term Memory)**

## LTSM

Dropout
- to prevent overfitting
- higher dropout rate should apply on layer with larger content/dimension/


### Bidirectional
- use both past and future information to get a better sense of current input.

Forward direction - past


Backward direction - future

Example:

He said, “Teddy
He said, “Teddy


### Credits:

https://hackernoon.com/understanding-architecture-of-lstm-cell-from-scratch-with-code-8da40f0b71f4
