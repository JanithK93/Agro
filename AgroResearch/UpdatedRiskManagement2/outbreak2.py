import numpy as np
import time, sys
from pygame import mixer


class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)

        # setting the number of nodes in layer 2 and layer 3
        l2 = 5
        l3 = 4

        # assign random weights to matrices in network
        # form at is (no. of nodes in previous layer) x (no. of nodes in following layer)
        self.synaptic_weights1 = 2 * np.random.random((3, l2)) - 1
        self.synaptic_weights2 = 2 * np.random.random((l2, l3)) - 1
        self.synaptic_weights3 = 2 * np.random.random((l3, 1)) - 1

    def __sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # derivative of sigmoid function, indicates confidence about existing weight
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # train neural network, adusting synaptic weights each time
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in xrange(number_of_training_iterations):
            # pass training set through our neural network
            # a2 means the activations fed to second layer
            a2 = self.__sigmoid(np.dot(training_set_inputs, self.synaptic_weights1))
            a3 = self.__sigmoid(np.dot(a2, self.synaptic_weights2))
            output = self.__sigmoid(np.dot(a3, self.synaptic_weights3))
            print("output while training")
            print(output)
            # calculate 'error'
            del4 = (training_set_outputs - output) * self.__sigmoid_derivative(output)
            #print("error in layer 4")
            #print(del4)

            if del4.all() > 0.0001:
                # find 'errors' in each layer
                del3 = np.dot(self.synaptic_weights3, del4.T) * (self.__sigmoid_derivative(a3).T)
                del2 = np.dot(self.synaptic_weights2, del3) * (self.__sigmoid_derivative(a2).T)

                # get adjustments (gradients) for each layer
                adjustment3 = np.dot(a3.T, del4)
                adjustment2 = np.dot(a2.T, del3.T)
                adjustment1 = np.dot(training_set_inputs.T, del2.T)

                # adjust weights accordingly
                self.synaptic_weights1 += adjustment1
                self.synaptic_weights2 += adjustment2
                self.synaptic_weights3 += adjustment3
        print("Ouput after training")
        print(output)

    def forward_pass(self, inputs):

        #take user entered values to separate variables in temperature in centigrades,humidity & sunlight value in lux
        temperature=inputs[0]
        sunlight = inputs[1]
        humidity=inputs[2]


        print("Newly Entered Temperature :" + str(temperature))
        print("Newly Entered Sunlight :" + str(sunlight))
        print("Newly Entered Humidity :" + str(humidity))

        # pass our inputs through our neural network
        a2 = self.__sigmoid(np.dot(inputs, self.synaptic_weights1))
        a3 = self.__sigmoid(np.dot(a2, self.synaptic_weights2))
        output = self.__sigmoid(np.dot(a3, self.synaptic_weights3))
        print("Predicted output :")
        print(output)
        roundedOutput = round(output,0)
        print("Predicted ouput approximately closer to :")
        print(roundedOutput)

        #If output closer to 1, warn about the disease occurence

        if roundedOutput == 1.0:
            #checking which weather condition causes for a disease to occur and warn about the condition.
            if 15 > temperature :
                mixer.init()
                sound = mixer.Sound("lowTemperatureWarning.wav")
                sound.play()
                time.sleep(1000)
            elif 35 < temperature:
                mixer.init()
                sound = mixer.Sound("highTemperatureWarning.wav")
                sound.play()
                time.sleep(1000)
            elif 1500 < sunlight :
                mixer.init()
                sound = mixer.Sound("tooMuchlightWarning.wav")
                sound.play()
                time.sleep(1000)
            elif 200 > sunlight :
                mixer.init()
                sound = mixer.Sound("lowLightWarning.wav")
                sound.play()
                sound.play()
                time.sleep(1000)
            elif 65 > humidity:
                mixer.init()
                sound = mixer.Sound("lowHumidityWarning.wav")
                sound.play()
                sound.play()
                time.sleep(1000)
        elif roundedOutput == 0.0:
            print("No threat of disease outbreak")



#Training dataset ->[temperature,sunlight,humidity]
training_set_inputs=np.array([[19,1002,89 ], [18,1080,85],[29,1002,79],[17,999,65],[37,1690,51],[41,1567,34],[23,908,99],[19,1580,31],
                                  [35,998,67],[16,897,64],[15,1002,67],[42,976,89],[25,980,76],[12,1000,91],[21,998,12],[35,1500,35],
                                  [39,1768,62],[22,1009,71],[30,1740,97],[36,1679,84],[19,1200,54],[23,1500,88],[32,1643,62],[33, 1001, 67],
                                  [11,1546,61],[32,990,21],[16,1003,98],[25,1689,42],[18,1576,67],[11,1345,34],[34,1007,68],[24,1000,98],
                                  [15,1690,64],[17,998,20],[19,978,89],[14,1002,65],[31,658,99],[20,1569,70],[31,1009,83],[45,1356,99],
                                  [28,761,75],[18,569,81],[26,893,94],[34,901,67],[11,256,41],[33,603,70],[18,752,99],[13,490,23],[34,568,68],
                                  [15,560,65],[20,591,69],[12,134,51],[17,641,70],[10,998,66],[18,800,69],[37,231,35],[16,711,78],[21,569,68],
                                  [37,609,85],[39,789,21],[38,458,32],[19,601,74],[26,671,65],[13,753,89],[34,543,80],[43,1764,43],[20,715,91],
                                  [22,521,64],[33,692,63],[12,959,70],[21,990,67],[34,712,68],[25,569,81],[14,741,64],[12,453,31],[18,201,55],
                                  [36,786,23],[21,678,99],[34,671,75],[11,781,43]
                                    ])
training_set_outputs = np.array(
    [[0], [0], [0], [0], [1], [1], [0], [1], [0], [0], [0], [1], [0], [0], [1], [1], [1], [0], [1], [1],
     [1], [1], [1], [0], [1], [1], [0], [1], [1], [1], [0], [0], [1], [1], [0], [0], [0], [1], [0], [1],
     [0], [0], [0], [0], [1], [0], [0], [1], [0], [0], [0], [1], [0], [1], [0], [1], [0], [0], [0], [1],
     [1], [0], [0], [0], [0], [1], [0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [0], [0], [1]
     ])

ann=NeuralNetwork()
ann.train(training_set_inputs,training_set_outputs,10000)
ann.forward_pass(np.array([11, 786, 23]))