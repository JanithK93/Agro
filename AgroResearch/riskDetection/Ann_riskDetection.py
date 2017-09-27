import math
import threading

from pybrain.tools.functions import sigmoid


class Connection:
    def __init__(self, connetedNeuron):
        self.connetedNeuron = connetedNeuron
        self.weight = 0.1
        self.dWeight = 0


class Neuron:
    eta = 0.9  # learning rate
    alpha = 0.15  # momentum rate

    def __init__(self, layer):
        self.dendrons = []  # defining inputs to neuron
        self.error = 0.0  # defining how much error it produce while giving the output
        self.output = 0.0
        self.gradient = 0.0

        # if the layer is input layer no need to create the connection,otherwise create the connection with the first layer
        if layer is None:
            pass
        else:
            for neuron in layer:
                con = Connection(neuron)
                self.dendrons.append(con)

    def addError(self, er):
        self.error == self.error + er

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def dSigmoid(self, x):
        return x * (1 - x)

    def feedForward(self):
        if (len(self.dendrons) == 0):
            return
        sumOfOutputs = 0.0
        for dendron in self.dendrons:
            sumOfOutputs = sumOfOutputs + dendron.connetedNeuron.output * dendron.weight
        self.output = self.sigmoid(sumOfOutputs)

    def BackPropergate(self):
        self.gradient = self.error * self.dSigmoid(self.output)
        for dendron in self.dendrons:
            dendron.dWeight = Neuron.eta * (dendron.connetedNeuron.output * self.gradient) + (Neuron.alpha * dendron.dWeight)
            dendron.weight = dendron.weight + dendron.dWeight
          #  dendron.connectedNeuron.addError(self.gradient * dendron.weight)
            dendron.connetedNeuron .addError(self.gradient * dendron.weight)
        self.error = 0.0


class Net:                              # Network class will use the Neuron class to create the network
    def __init__(self, topology):       # topology will hold how many neurons will each layer have
        self.layers = []
        for numNeuron in topology:      # numNeuron holds the no of neuron in each layer
            layer = []
            for i in range(numNeuron):
                if (len(self.layers) == 0):  # if previous layer is the input layer don't connect the neurons,else connect the previous layers' neurons
                    neuron = Neuron(None)
                else:
                    neuron = Neuron(self.layers[-1])
                layer.append(neuron)
            layer.append(Neuron(None))
            layer[-1].output = 1
            self.layers.append(layer)

    def setInputs(self, inputs):            # This supplies the inputs to the input neurons
        for i in range(len(inputs)):
            self.layers[0][i].output = inputs[i]

    def feedForward(self):
        for layer in self.layers:
            for neuron in layer:
                neuron.feedForward()

    def backPropagate(self, targets):
        for i in range(len(targets)):
            self.layers[-1][i].error = targets[i] - self.layers[-1][i].output

        for layer in self.layers[::-1]:
            for neuron in layer:
                neuron.BackPropergate()

    def getError(self, targets):
        avgErr = 0
        for i in range(len(targets)):
            err = targets[i] - self.layers[-1][i].output
            avgErr = avgErr + (err * err)
        avgErr = avgErr / len(targets)
        return avgErr

    def  getOuptputs(self):
        outputs = []
        for neuron in self.layers[-1]:
            outputs.append(neuron.output)
        return outputs

def main():
    net = Net([5, 6, 4,1])          # This line constructs the Net.first layer has 2 neurons, we can have as much hidden layers we want & the last layer contains 1 output.
    inputs = [[30,73,668,354000,15.8192090395],
              [28,85,0,210800,42.3809524],
              [34,61,970,120225,74.062383],
              [29,78,270,150150,85.0532801],
              [29,81,267,452600,95.1634998],
              [31,69,926,356289,26.950874]]
    ouputs = [[0], [1], [2], [3],[3],[1]]


    while True:                             # Training the network
        err = 0
        for i in range(len(inputs)):
            print "Input=" + str(inputs[i])
            net.setInputs(inputs[i])    # Here we need to set the inputs to the input layer,
            net.feedForward()           # feedforward,calculate the error & Back propagate
            net.backPropagate(ouputs[i])
            err = err + net.getError(ouputs[i])
            print "Output=" + str(net.getOuptputs())
            print "Error=" + str(net.getError(ouputs[i]))  # for each input a error is creating here we are calculating the avg error of all the errors
        err = err / len(inputs)
        print "Average Error= "+ str(err)
        if (err < 0.1):                     # if error is less than some threshold value, then stop the training
            break

#Here We are testing the network
from ImageIdList import idList
Id = idList()
from areaCalculation import arr
intialAreaArray = arr()



def riskDetection(imagId,temperature,humidity,sunlight,diseasedSpotArea):
    #This function is called every 2 hours periodically
    #threading.Timer(1440.0, getDiseasedLeafSpot).start()

    if imagId not in Id:
        Id[imagId] = imagId
        intialAreaArray[imagId] = diseasedSpotArea
        changedRate=0.0
        print(intialAreaArray)
        print(Id)
    elif imagId in Id:
        changedRate = intialAreaArray.calculateChangeInArea(intialAreaArray, imagId, diseasedSpotArea)
        print(changedRate)

    temp = temperature
    H = humidity
    light = sunlight
    spotArea=intialAreaArray[imagId]
    changedRateOfInitialSpotArea=changedRate
    net = Net([5, 6, 4, 1])

    i = [temp, H, light, spotArea, changedRateOfInitialSpotArea]
    #while True:
    net.setInputs(i)             #For testing we don't need backPropergation,It needs only for training
    net.feedForward()
    riskLevel= net.getOuptputs()
    print(riskLevel)
    riskLevel=round(riskLevel[0],0)
    print(int(riskLevel))

   #Warn the User
    from Warnings import userWarning
    warning=userWarning()
    warning.turnAlarmOn()
    warning.say(int(riskLevel))


#To train the network
#main()
riskDetection(1,28,78,588,1054000)         #Just a random value for testing purpose


