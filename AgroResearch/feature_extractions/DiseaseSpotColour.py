import cv2
import numpy as np
import glob
from matplotlib import pyplot as plt




def  SpotColour (image):

        img1 = image

      
        imgRead1 = cv2.imread(img1, 1)

        z1 = imgRead1.reshape((-1, 3))
        z1 = np.float32(z1)

        criteria1 = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 20.0)
        K1 = 25
        ret1, label1, center1 = cv2.kmeans(z1, K1, None, criteria1, 10, cv2.KMEANS_RANDOM_CENTERS)

        center1 = np.uint8(center1)

        res1 = center1[label1.flatten()]

        res011 = res1.reshape((imgRead1.shape))

        # gray image
        imgray1 = cv2.cvtColor(res011, cv2.COLOR_BGR2GRAY)

        # erosion
        kernel011 = np.ones((5, 5), np.uint8)
        erosion011 = cv2.erode(imgray1, kernel011, iterations=1)

        ret1, th_gray1 = cv2.threshold(erosion011, 100, 255, 0)

        # range the green colour
        # l_green= np.array([36,0,0])
        # u_green = np.array([86,255,255])

        lower_green = np.array([36, 0, 0], dtype=np.uint8)
        upper_green = np.array([86, 255, 255], dtype=np.uint8)

        # l_green= np.array([36,0,0])
        # u_green = np.array([86,255,255])



        # Hsv_image
        # hsv_img = cv2.cvtColor(imgRead,cv2.COLOR_BGR2HSV)



        # threshold an image to get only green colour area

        mask_green1 = cv2.inRange(res011, lower_green, upper_green)

        # Bitwise-AND mask to identify green area
        # res_maskGreen = cv2.bitwise_and(res01,res01,mask = mask_green)

        # Bitwise-NOT mask and original image
        res_maskSpots1 = cv2.bitwise_not(res011, res011, mask=mask_green1)

        # draw contour to identify spot area
        _, cntsSpots1, hierachy1 = cv2.findContours(mask_green1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Contour Approximation

        # max_Cntarea = max(cntsSpots, key=cv2.contourArea)
        # epsilon = 0.5 * cv2.arcLength(cntsSpots, True)
        # approx = cv2.approxPolyDP(cntsSpots, epsilon, True)



        cv2.drawContours(res_maskSpots1, cntsSpots1, -1, [0, 0, 255], 5)

        # ierachy = hierachy[0] # get the actual inner list of hierarchy descriptions
        #
        # For each contour, find the bounding rectangle and draw it
        # or component in zip(cntsSpots, hierachy):
        #   currentContour = component[0]
        #   currentHierarchy = component[1]
        #   x,y,w,h = cv2.boundingRect(currentContour)
        #   if currentHierarchy[2] < 0:
        #       # these are the innermost child components
        #       cv2.rectangle(res_maskSpots,(x,y),(x+w,y+h),(0,0,255),3)
        #   elif currentHierarchy[3] < 0:
        #       # these are the outermost parent components
        #       cv2.rectangle(res_maskSpots,(x,y),(x+w,y+h),(0,255,0),3)


        mean_val = cv2.mean(res_maskSpots1, mask=mask_green1)
        print 'Average Spot Colour -->>> ' + str(mean_val)
        print '-----------------------------'

        # Show-image
        #   numpy_horizontl = np.hstack((imgRead, erosion01))
        #   numpy_horizontl_conct = np.concatenate((imgRead, erosion01), axis=1)

        #cv2.namedWindow('resized_w01', cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('resized_w01', 400, 450)
        #
        #cv2.namedWindow('resized_w02', cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('resized_w02', 400, 450)
        #
        ## cv2.namedWindow('resized_w03', cv2.WINDOW_NORMAL)
        ## cv2.resizeWindow('resized_w03', 400, 450)
        #
        #cv2.imshow('resized_w01', imgRead1)
        #cv2.imshow('resized_w02', mask_green1)
        ## cv2.imshow('resized_w03', res_maskGreen)
        #cv2.waitKey(5000)
        #cv2.destroyAllWindows()
        #