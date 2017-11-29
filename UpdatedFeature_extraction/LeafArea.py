import cv2
import numpy as np
import glob
from matplotlib import pyplot as plt

#for img in glob.glob('C:/Users/User/PycharmProjects/Last_29/Normal/*.jpg'):
def leafArea(image):

    img0 = image
    imgRead0 = cv2.imread(img0, 1)




    z0 = imgRead0.reshape((-1, 3))
    z0 = np.float32(z0)

    criteria0 = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 20.0)
    K0 = 3
    ret0, label0, center0 = cv2.kmeans(z0, K0, None, criteria0, 20, cv2.KMEANS_RANDOM_CENTERS)

    center0 = np.uint8(center0)

    res0 = center0[label0.flatten()]

    res010 = res0.reshape((imgRead0.shape))




    blur0 = cv2.blur(imgRead0, (3, 3))



    #range for green
    l_green0 = np.array([36, 0, 0])
    u_green0 = np.array([86,255,255])

    thresh = cv2.inRange(blur0, l_green0, u_green0)

    res_mask0 = cv2.bitwise_and(blur0, blur0, mask=thresh)

    thresh20 = thresh.copy()





    # erosion
    kernel010 = np.ones((5, 5), np.uint8)
    erosion010 = cv2.erode(thresh, kernel010, iterations=1)





    #bit_andImg = cv2.bitwise_and(res01, res01, mask=thresh)

    _, cnts0, _ = cv2.findContours(erosion010, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)



    # finding contour with maximum area and store it as best_cnt
    max_area = 0
    best_cnt0 = 1
    for cnt in cnts0:
        area0 = cv2.contourArea(cnt)
        if area0 > max_area:
            max_area = area0
            best_cnt0 = cnt


    print 'Green area detected -->>' + str(max_area)




   ## finding centroids of best_cnt and draw a circle there
   #M = cv2.moments(best_cnt)
   #cx, cy = int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])
   ## if best_cnt>1:
   #cv2.circle(res01, (cx, cy), 10, (0, 0, 255), -1)


    cv2.drawContours(res_mask0,best_cnt0,-1,[0,0,255],10)



    # Show_image
#cv2.namedWindow('resized_w01', cv2.WINDOW_NORMAL)
#cv2.resizeWindow('resized_w01', 400, 450)
#
#cv2.namedWindow('resized_w02', cv2.WINDOW_NORMAL)
#cv2.resizeWindow('resized_w02', 400, 450)
#
#
#cv2.imshow('resized_w01', res_mask0)
#cv2.imshow('resized_w02', imgRead0)
#
#
#cv2.waitKey(50000)
#cv2.destroyAllWindows()
#
