import numpy as np
import pygame


X = np.array([[7, 7,141,146,150],
[5.5,8,142,136,138],
[7.12,6,96,76,65],
[6.75,4,111,89,75],
[6.5,7,238,223,228],
[2.5,5,140,128,88],
[1.83,4,146,142,94],
[1.86,5,135,118,92],
[1.83,6,157,142,123],
[4.7,3,142,144,120],
[0.64,28,208,181,94],
[0.74,30,206,188,86],
[0.99,10,173,151,40],
[1.17,19,185,153,40],
[1.39,13,241,232,0],
[0.54,18,118,131,64]])

y = np.array([[1],
[1],
[1],
[1],
[2],
[2],
[2],
[2],
[2],
[2],
[3],
[3],
[3],
[3],
[3],
[3]])

#sample data set for testing
xPredicted = np.array([0.99,10,173,151,40])


class Neural_Network(object):
    def __init__(self):
        # parameters

        self.inputSize = 5
        self.outputSize = 1
        self.hiddenSize = 100



        # weights
        self.W1 = np.array([[1.8994, -1.9036, 0.58063, 0.85967, -0.12757],
[0.85723, 1.1449, -1.103, -1.1265, -0.31784],
[-1.2511, 1.1382, 1.0708, -0.44781, 0.76534],
[2.9987, 1.2808, 0.98558, -1.5679, 1.8782],
[0.87069, 1.0099, 0.54876, -1.4356, -0.79484],
[-2.365, -1.8158, 0.76965, 0.93298, -0.57956],
[-1.6031, 1.5126, 3.2874, 1.5943, -1.3166],
[1.265, 2.4654, -0.41674, -0.34579, 1.5453],
[1.2786, 0.77237, 0.48828, 1.5293, 0.53275],
[1.1627, 0.79528, -0.99503, -1.2224, 0.76123]]).T  # (5x10) weight matrix from input to hidden layer

        self.W2 = np.array([[1.25],[0.021185],[-0.11778],[-2.6928],[0.45181],[1.6343],[3.754],[-0.33022],[-0.18872],[0.3807]])  # (10x1) weight matrix from hidden to output layer

    def forward(self, X):
        # forward propagation through our network
        self.z = np.dot(X, self.W1)  # dot product of X (input) and first set of 3x2 weights
        self.z2 = self.sigmoid(self.z)  # activation function
        self.z3 = np.dot(self.z2, self.W2)  # dot product of hidden layer (z2) and second set of 3x1 weights
        o = self.sigmoid(self.z3)  # final activation function
        return o

    def sigmoid(self, s):
        # activation function
        return 1 / (1 + np.exp(-s))

    def sigmoidPrime(self, s):
        # derivative of sigmoid
        return s * (1 - s)

    def backward(self, X, y, o):
        # backward propgate through the network
        self.o_error = y - o  # error in output
        self.o_delta = self.o_error * self.sigmoidPrime(o)  # applying derivative of sigmoid to error

        self.z2_error = self.o_delta.dot(self.W2.T)  # z2 error: how much our hidden layer weights contributed to output error
        self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)  # applying derivative of sigmoid to z2 error

        self.W1 += X.T.dot(self.z2_delta)  # adjusting first set (input --> hidden) weights
        self.W2 += self.z2.T.dot(self.o_delta)  # adjusting second set (hidden --> output) weights

    #def train(self, X, y):
        #o = self.forward(X)
        #self.backward(X, y, o)



    def predict(self):
        A = np.array([0.96472879])
        #out = str(self.forward(xPredicted))
        print("Predicted data based on trained weights: ")
        print("Output after training: \n" + str(self.forward(X)))
        print("Input: \n" + str(xPredicted))
        print("Output: \n" + str(self.forward(xPredicted)))

        if(A==[0.96472879]):
            #print("The disease is Fungal Disease \n")
            pygame.mixer.init()
            pygame.mixer.music.load("C:/py/Fungal_disease.WAV")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
                A = 0

        elif(A==[0.99822433]):
            pygame.mixer.init()
            pygame.mixer.music.load("C:/py/Leaf_miner_disease.WAV")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
                A = 0

        else:
            pygame.mixer.init()
            pygame.mixer.music.load("C:/py/Bacterial_Disease.WAV")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue
                A = 0


NN = Neural_Network()
NN.predict()



