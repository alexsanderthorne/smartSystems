import numpy as np

mmatrix1 = np.array([[1, 2, 3], [4, 5, 6]])

# ReLu function


def relu(X):
    return np.maximum(0, X)


print(relu(mmatrix1))

# softmax function


def softmax(X):
    expo = np.exp(X)
    expo_sum = np.sum(np.exp(X))
    return expo/expo_sum

#print (softmax(mmatrix1))

# sigmoid function


def sigmoid(X):
    return 1/(1+np.exp(-X))  # Example with mmatrix defined above


print(sigmoid(mmatrix1))
