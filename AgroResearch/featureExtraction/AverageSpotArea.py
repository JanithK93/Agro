import cv2
import numpy as np
import glob
from matplotlib import pyplot as plt

#for img in glob.glob('C:/Users/User/PycharmProjects/researchP/Diseased_L/*.jpg'):

def  averageSpotArea (image):

    img2 = image
    imgRead2 = cv2.imread(img2, 1)


    z2 = imgRead2.reshape((-1, 3))
    z2 = np.float32(z2)

    criteria2 = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 20.0)
    K2 = 25
    ret2, label2, center2 = cv2.kmeans(z2, K2, None, criteria2, 10, cv2.KMEANS_RANDOM_CENTERS)

    center2 = np.uint8(center2)

    res2 = center2[label2.flatten()]

    res012 = res2.reshape((imgRead2.shape))







     #gray image
    imgray2 = cv2.cvtColor(res012, cv2.COLOR_BGR2GRAY)


    # erosion
    kernel012 = np.ones((5, 5), np.uint8)
    erosion012 = cv2.erode(imgray2, kernel012, iterations=1)

    ret2, th_gray2 = cv2.threshold(erosion012, 100, 255, 0)


    #range the green colour
    #l_green= np.array([36,0,0])
    #u_green = np.array([86,255,255])

    lower_c2 = np.array([36, 0, 0 ], dtype=np.uint8)
    upper_c2 = np.array([86, 255, 255], dtype=np.uint8)



    #l_green= np.array([36,0,0])
    #u_green = np.array([86,255,255])



    #Hsv_image
    #hsv_img = cv2.cvtColor(imgRead,cv2.COLOR_BGR2HSV)



    # threshold an image to get only green colour area

    mask_c2 = cv2.inRange(res012,lower_c2,upper_c2)


    #Bitwise-AND mask to identify green area
    #res_maskGreen = cv2.bitwise_and(res01,res01,mask = mask_green)

     # Bitwise-NOT mask and original image
    res_maskSpots2 = cv2.bitwise_not(res012,res012 , mask=mask_c2)


    # draw contour to identify spot area
    _, cntsSpots2,hierachy2 = cv2.findContours(mask_c2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)







    max_area2 = max(cntsSpots2,key=cv2.contourArea)


    cv2.drawContours(res_maskSpots2, cntsSpots2, -1, [0,0,255],5)

     #Contour Approximation
    epsilon2 = 0.1 * cv2.arcLength(max_area2,True)
    approx2 = cv2.approxPolyDP(max_area2,epsilon2,True)

    spot_area2 = cv2.contourArea(max_area2)

    #print  cntsSpots










    #print  area

    print 'detected area in the spot -->>  ' + str(spot_area2)
























    #cv2.namedWindow('resized_w01', cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('resized_w01', 400, 450)
    #
    #cv2.namedWindow('resized_w02', cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('resized_w02', 400, 450)
    #
    ##cv2.namedWindow('resized_w03', cv2.WINDOW_NORMAL)
    ##cv2.resizeWindow('resized_w03', 400, 450)
    #
    #cv2.imshow('resized_w01', imgRead2)
    #cv2.imshow('resized_w02', res_maskSpots2)
    ##cv2.imshow('resized_w03', res_maskGreen2)
    #cv2.waitKey(500000)
    #cv2.destroyAllWindows()
    #