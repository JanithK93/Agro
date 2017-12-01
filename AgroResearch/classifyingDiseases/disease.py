import numpy as np
import time, sys
import pygame
from numpy import array,dot

class NeuralNetwork():
    def __init__(self):

        input_layer = 3
        hidden_layer1 = 3
        hidden_layer2 = 4
        output_neurones = 1

        # assign random weights to matrices in network
        # form at is (no. of nodes in previous layer) x (no. of nodes in following layer)
        self.w1 = 2 * np.random.random((input_layer,  hidden_layer1)) - 1
        self.w2 = 2 * np.random.random(( hidden_layer1,  hidden_layer2)) - 1
        self.w3 = 2 * np.random.random(( hidden_layer2, output_neurones)) - 1

        np.random.seed(1)

    def __sigmoid(self, s):
        return 1 / (1 + np.exp(-s))


    def __sigmoid_derivative(self, s):
        return s * (1 - s)

    # train neural network, adusting synaptic weights each time
    def train(self,X, Y,iterations):
        for iteration in xrange(iterations):
            # pass training set through our neural network
            # a2 means the activations fed to second layer

            hidden2_activation = self.__sigmoid(np.dot(X, self.w1))
            hidden3_activation = self.__sigmoid(np.dot( hidden2_activation, self.w2))
            output = self.__sigmoid(np.dot( hidden3_activation, self.w3))

            print(output)
            # calculate 'error'
            error_1 = (Y - output) * self.__sigmoid_derivative(output)
            #print("error in layer 4")
            #print(del4)

            if error_1.any() > 0.0001:
                # find 'errors' in each layer
                error_2 = np.dot(self.w3, error_1.T) * (self.__sigmoid_derivative( hidden3_activation).T)
                error_3 = np.dot(self.w2, error_2) * (self.__sigmoid_derivative( hidden2_activation).T)


                update_1 = np.dot( hidden3_activation.T, error_1)
                update_2 = np.dot( hidden2_activation.T,error_2.T)
                update_3 = np.dot(X.T, error_3.T)


                self.w1 += update_3
                self.w2 += update_2
                self.w3 += update_1

        print(output)

    def forward_pass(self, input):
        spot_colour = input[0]
        # pass our inputs through our neural network
        hidden2_activation = self.__sigmoid(np.dot(input, self.w1))
        hidden3_activation = self.__sigmoid(np.dot( hidden2_activation, self.w2))
        output = self.__sigmoid(np.dot( hidden3_activation, self.w3))

        print(output)
        round_off_val = round(output,0)

        print(round_off_val)

        #If output closer to 1, warn about the disease occurence

        if round_off_val == 1.0:
            #checking which weather condition causes for a disease to occur and warn about the condition.
            pygame.mixer.init()
            pygame.mixer.music.load( "C:/Users/Toshiba/Desktop/Agro/AgroResearch/audioFile/This_is_Early_Leaf_Spot_Disease_Reduce_the_humidit.wav")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue

        elif round_off_val == 2.0:
            pygame.mixer.init()
            pygame.mixer.music.load("C:/Users/Toshiba/Desktop/Agro/AgroResearch/audioFile/This_is_bacterial_wilt_Use_fungicides_containing_p.wav")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue

        elif round_off_val == 3.0:
            pygame.mixer.init()
            pygame.mixer.music.load("C:/Users/Toshiba/Desktop/Agro/AgroResearch/audioFile/This_is_fungal_disease_Move_the_plant_to_a_cooler_place.wav")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue

        else:
            pygame.mixer.init()
            pygame.mixer.music.load("C:/Users/Toshiba/Desktop/Agro/AgroResearch/audioFile/Sorry_The_disease_cannot_be_clearly_identified_.wav")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                continue

if __name__ == "__main__":
	# initialise single neuron neural network
	neural_network = NeuralNetwork()

	# the training set.
	X = array([[149.731221733349,107.114544515211,199.460054564164],[68.6416519537827,55.8033759746031,218.846680749285],[68.64451829,52.9777224,217.4130397],
              [117.440511698119,83.7555917746448,180.669432770256],[79.5307899766109,54.7177590127269,202.387018790367],[115.512597098621,91.7372797427704,193.980959451717],
              [87.8255406922620,70.7380316517090,208.34340681211],[93.2089206068959,72.9915794487375,199.314700947901],[115.512597098621,91.7372797427704,193.980959451717],
              [48.7120891396242,39.1525104071235,228.248701801758],[137.131538489425,84.8667600902265,153.076439815599],[109.936463636895,80.4749977391620,193.649988734330],
              [158.537729592086,124.731288600566,163.034148310133],[120.952692090567,79.5907332279454,165.400395092019],[132.080755445937,91.5718786614012,175.702259841346],
              [137.854538942581,67.4048525102217,157.291021352251],[137.854538942581,67.4048525102217,157.291021352251],[149.154203491859,105.498468059232,167.504981440337],
              [90.8514315900345,63.5653502253760,201.296844618204],[159.471947332504,121.441438429901,178.324205809044],[142.193104764951,108.887494606744,182.360852437752],
              [96.5324177311855,58.1887206135137,202.379291959550],[115.121704454372,70.7661088836838,188.577903776435],[126.160624523665,102.933493884209,198.051653128871],
              [158.120739831733,111.030404695687,166.413255387069],[165.198569973961,109.665891218804,149.238778816083],[116.693087326302,83.7394896642969,175.083526213002],
              [112.055942020853,82.8518624876703,201.343731862950],[113.779857220257,91.2656480861778,193.134238454919],[166.356989969187,118.057488961563,172.887440860326],
              [128.022373181511,97.3074043164747,189.530273403295],[127.569964575311,93.3223376144609,198.428596016940],[128.947074238076,104.125777799688,192.471421286552],
              [134.429640068523,107.450307064711,196.442839096678],[161.209794507776,123.733854004799,183.737410897428],[159.415206331261,137.126665863567,193.155147724874],
              [136.941958270568,111.470022330685,191.212136869677],[129.514169500638,96.9752049274972,193.488714468071],[141.143392801974,109.666991809662,193.603048864159],
              [126.944137674127,100.292890243324,192.613234947555],[117.526692990202,62.3249017271792,177.055847370473],[136.760764378235,83.4619467214385,162.633915754575],
              [132.722668035656,72.6584110258745,166.282082524367],[107.405468215029,58.7716708577216,171.657203793031],[139.360302888721,94.7603154452053,158.342790168130],
              [150.511843547844,120.376350280538,170.943348102443],[131.135875551753,124.779745695825,218.384167919976],[113.892669952373,96.5335081821516,208.975053872458],
              [97.0483430474556,74.1792216558961,204.256971318450],[119.393403379848,89.3488200809182,196.956347260067],[89.7818611899798,68.7578991814792,210.093294578156],
              [52.86953717979435,45.58293155589291,235.4669256644951],[78.31730243250904,54.498973947040604,210.4460223974496],[151.64012631686631,121.15779554743881,187.98818809300008],
              [144.50557327612657,108.77768535529432,169.712503209114],[135.2635866980183,85.2368124252256,167.81429199761394],[130.93884434570188,79.30679639775332,166.99106774377867],
              [123.63404889061876,81.69136510196492,175.03113471925263],[141.42342362322307,103.43572620814673,177.45767545909285],[120.12353094849551,86.49749760227891,177.33265821380516],
              [148.59832960543875, 83.17839218472814, 163.8717097467748],[151.6200965587524, 92.35774267169035, 167.73580928591448],[141.96642370088182, 102.61968077097667, 187.33708103271462],
              [130.62412568235746, 87.09218392698847, 184.17276784285033],[160.55549575498003, 133.15586818729702, 178.48111252010173],[142.6955824787757, 92.29699308908297,170.519596927736]])

	Y = array([[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[2],[3],[3],[3],[3],[3],[3],[3],[3],[3],[3],[3],[3],[3],[3],[3]])


	neural_network.train(X, Y, 10000)


	# test with new input

	print neural_network.forward_pass(array([127.569964575311,93.3223376144609,198.428596016940]))