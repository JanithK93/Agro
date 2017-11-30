import cv2
import numpy as np
import glob
from matplotlib import pyplot as plt

#for img22 in glob.glob('C:/Users/User/PycharmProjects/researchP/Diseased_L/DSC_0387.jpg'):

def spotarea22(image) :
    img22 = image

    imgRead22 = cv2.imread(img22, 1)



    z = imgRead22.reshape((-1, 3))
    z = np.float32(z)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 4
    ret, label, center = cv2.kmeans(z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)

    res = center[label.flatten()]

    res0122 = res.reshape((imgRead22.shape))

    imgray22 = cv2.cvtColor(res0122, cv2.COLOR_BGR2GRAY)

    # erosion
    kernel0122 = np.ones((5, 5), np.uint8)
    erosion0122 = cv2.erode(imgray22, kernel0122, iterations=1)

    ret22, th_gray22 = cv2.threshold(erosion0122, 127, 255, 0)

    bit_andImg22 = cv2.bitwise_and(res0122, res0122, mask=th_gray22)

    _, cnts22, _ = cv2.findContours(th_gray22, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts22) != 0:
        #        cv2.drawContours(bit_andImg,cnts,-1,[0,0,255],10)

        max_area22 = max(cnts22, key=cv2.contourArea)

        cv2.drawContours(bit_andImg22, max_area22, -1, [0, 0, 255], 10)

        # Contour Approximation
        epsilon22 = 0.1 * cv2.arcLength(max_area22, True)
        approx22 = cv2.approxPolyDP(max_area22, epsilon22, True)

        area22 = cv2.contourArea(max_area22)

        # print  area

        print 'detected area in the spot -->>  ' + str(area22)
        #mean_val = cv2.mean(bit_andImg22, mask=mask_green1)
        #print 'Average Spot Colour -->>> ' + str(mean_val)
        #print '-----------------------------'

        # print 'detected area in the  spot -->>  ' + str(np.countNonZero(max_area))

        #equa_diameter = np.sqrt(4 * area / np.pi)

        #print 'detected diameter in the spot -->>  ' + str(equa_diameter)

        # finalnpzero = np.zeros(imgRead.shape,np.uint8)
        # masknpzero = np.zeros(imgray.shape,np.uint8)
        #
        # for i in xrange(0,len(cnts)) :
        #    masknpzero[...] =0
        #    cv2.drawContours(masknpzero,cnts,i,255,-1)
        #    cv2.drawContours(finalnpzero,cnts,i,cv2.mean(imgRead,masknpzero),-1)
        #
        #    print 'average color of the detected spot-->>' +str(cv2.mean(imgRead,masknpzero))
        #

















        #show_image
        #cv2.namedWindow('resized_w01', cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('resized_w01', 400, 750)
        #
        #cv2.namedWindow('resized_w02', cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('resized_w02', 400, 750)
        #
        #
        #cv2.imshow('resized_w01', bit_andImg22)
        #cv2.imshow('resized_w02',imgRead22)
        #cv2.waitKey(500000)
        #cv2.destroyAllWindows()
        #
        #  print approx
        #  print '**************************************'




