import cv2
import numpy as np
import glob
from matplotlib import pyplot as plt

#for img in glob.glob('C:/Users/User/PycharmProjects/researchP/Normal_L/*.jpg'):

def  leafArea (image):

    imgbu = image

    imgReadbu = cv2.imread(imgbu, 1)

    cv2.namedWindow('resized_w01', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('resized_w01', 400, 550)

    zbu = imgReadbu.reshape((-1, 3))
    zbu = np.float32(zbu)

    criteriabu = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 10.0)
    Kbu = 4
    retbu, labelbu, centerbu = cv2.kmeans(zbu, Kbu, None, criteriabu, 10, cv2.KMEANS_RANDOM_CENTERS)

    centerbu = np.uint8(centerbu)

    resbu = centerbu[labelbu.flatten()]

    res01bu = resbu.reshape((imgReadbu.shape))

    imgraybu = cv2.cvtColor(res01bu, cv2.COLOR_BGR2GRAY)

    # erosion
    kernel01bu = np.ones((5, 5), np.uint8)
    erosion01bu = cv2.erode(imgraybu, kernel01bu, iterations=1)

    retbu, th_graybu = cv2.threshold(erosion01bu, 80, 255, 0)

    bit_andImgbu = cv2.bitwise_and(res01bu, res01bu, mask=th_graybu)

    _, cntsbu, _ = cv2.findContours(th_graybu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(cntsbu) != 0:
        #        cv2.drawContours(bit_andImg,cnts,-1,[0,0,255],10)

        max_areabu = max(cntsbu, key=cv2.contourArea)

        cv2.drawContours(bit_andImgbu, max_areabu, -1, [0, 0, 255], 10)

        # Contour Approximation
        epsilonbu = 0.1 * cv2.arcLength(max_areabu, True)
        approxbu = cv2.approxPolyDP(max_areabu, epsilonbu, True)

        areabu = cv2.contourArea(max_areabu)

        # print  area

        print 'detected area in the spot -->>  ' + str(areabu)

      # # print 'detected area in the  spot -->>  ' + str(np.countNonZero(max_area))
      #
      # equa_diameter = np.sqrt(4 * areabu/ np.pi)
      #
      # # print 'detected diameter in the spot -->>  ' + str(equa_diameter)
      #
      # # print 'detected average colour of spot -->>  ' + str(area.mean())





        # print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

        #   cv2.imshow('resized_w01', bit_andImg)
        #   cv2.waitKey(5000)
        #   cv2.destroyAllWindows()
        #
        #  print approx
        #  print '**************************************'

    ## Show-image
    #numpy_horizontl = np.hstack((imgRead, bit_andImg))
    #numpy_horizontl_conct = np.concatenate((imgRead, bit_andImg), axis=1)
    #
    #cv2.namedWindow('resized_w01', cv2.WINDOW_NORMAL)
    #cv2.resizeWindow('resized_w01', 800, 550)
    #
    #cv2.imshow('resized_w01', numpy_horizontl_conct)
    #cv2.waitKey(5000)
    #cv2.destroyAllWindows()


    #Show_image
        #cv2.namedWindow('resized_w01', cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('resized_w01', 400, 450)
        #
        #cv2.namedWindow('resized_w02', cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('resized_w02', 400, 450)
        #
        ##cv2.namedWindow('resized_w03', cv2.WINDOW_NORMAL)
        ##cv2.resizeWindow('resized_w03', 400, 450)
        #
        #cv2.imshow('resized_w01', imgReadbu)
        #cv2.imshow('resized_w02', res_maskSpotsbu)
        ##cv2.imshow('resized_w03', res_maskGreen2)
        #cv2.waitKey(500000)
        #cv2.destroyAllWindows()