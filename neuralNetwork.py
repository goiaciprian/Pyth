# usr/bin/env python

import numpy as np


class NeuralNetwork:
    def __init__(self):
        # * parameters
        self.inputSize = 2
        self.outputSize = 1
        self.hiddenSize = 3

        # * weights
        # (3x2) weight matrix from input to hidden layer
        self.W1 = np.random.randn(self.inputSize, self.hiddenSize)
        # (3x1) weight matrix from hidden layer to output
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize)

    def forward(self, x):
        # * forward propagation through out network
        # dot product of x (input) and first set of 3x2 matrix
        self.z = np.dot(x, self.W1)
        # activation function
        self.z2 = self.sigmoid(self.z)
        # dot product of hidden layer (z2) and second set of 3x1 matrix
        self.z3 = np.dot(self.z2, self.W2)
        # final activation function
        o = self.sigmoid(self.z3)
        return o

    def sigmoid(self, s):
        # activation function
        return 1/(1+np.exp(-s))

    def sigmoidPrime(self, s):
        # derivative of sigmoid
        return s * (1-s)

    def backward(self, x, y, o):
        # backward propogate through the network
        self.o_error = y - o  # error in output
        # applaying derivate of sigmoid to error
        self.o_delta = self.o_error * self.sigmoidPrime(o)

        # z2 error: how much our hidden layer weights contribuited to output
        self.z2_error = self.o_delta.dot(self.W2.T)
        # applaying derivate of sigmoid to z2 error
        self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2_error)

        # adjusting first set (input ---> hidden) weights
        self.W1 += x.T.dot(self.z2_delta)
        # adjusting second set (hidden ---> output) weights
        self.W2 += self.z2.T.dot(self.o_delta)

    def train(self, x, y):
        o = self.forward(x)
        self.backward(x, y, o)

    def saveWeights(self):
        np.savetxt("w1.txt", self.W1, fmt="%s")
        np.savetxt("w2.txt", self.W2, fmt="%s")

    def predict(self):
        print("Predicted data based on trained weights: ")
        print("Input (scaled): \n" + str(xPredicted))
        print("Output: \n" + str(self.forward(xPredicted)))


if __name__ == "__main__":

    # x = (hours sleeping, hours studying), y = score on test
    x = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
    y = np.array(([92], [86], [89]), dtype=float)
    xPredicted = np.array((4, 8), dtype=float)

    # scale units
    x = x/np.amax(x, axis=0)
    xPredicted = xPredicted/np.amax(xPredicted, axis=0)
    y = y/100

    NN = NeuralNetwork()
    for i in range(10):
        print("# " + str(i) + "\n")
        print("Input (scaled): \n" + str(x))
        print("Actual output: \n" + str(y))
        print("Predicted output: \n" + str(NN.forward(x)))
        print("Loss: \n" + str(np.mean(np.square(y-NN.forward(x)))))
        print("\n")

    NN.saveWeights()
    NN.predict()
