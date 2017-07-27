import cv2
import PIL
import os
import numpy as np
from matplotlib import pyplot as plt
import time

lastShape = 0

# go back and redo at smaller intervals

def recheck(logo, marketMap, size):
    size = int(size*100)
    for s in range(size-7, size+7):
        sizex = (float(s)/100)
        min_val, max_val, min_loc, max_loc, res, img = matchTheTemplate(marketMap, logo, sizex)
        if max_val > .8:
            return min_val, max_val, min_loc, max_loc
            break
        else:
            continue
        break


# Take the image, template and ratio size --> min_val, max_val, min_loc, max_loc, res, img
# Actual template matching algorithm
def matchTheTemplate(img, template, sizex):

    # img = cv2.imread(img, 0)
    # time.sleep(2)

    # template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
    #
    # template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)


    # template = cv2.imread(template, 0)
    template = cv2.resize(template, (0, 0), fx=sizex, fy=sizex)
    w, h = template.shape[::-1]
    # print "w: {} h: {}".format(w, h)

    # Types of matchers, [1] is the best so far
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    method = eval(methods[1])

    # Apply template Matching
    # print img
    res = cv2.matchTemplate(img, template, method)
    # print "Gets this far"
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print min_val, max_val, min_loc, max_loc

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    # print top_left, bottom_right
    return min_val, max_val, min_loc, max_loc, res, img


def isFound(max_val, img, res):
    if max_val > .8:
        # plt.subplot(121), plt.imshow(res, cmap='gray')
        # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        # plt.subplot(122), plt.imshow(img, cmap='gray')
        # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        # plt.suptitle(method)
        # plt.show()
        return True
    else:
        return False


def searchLogoInMap(logo, marketMap):

    highest = 0
    h, w = logo.shape[:2]

    print h, w
    estimatedScaler = int((68/float(h))*10-1)
    print estimatedScaler


    # Template matching requires same size to create match
    # for each size get the score
    # Another idea to try: get dimensions of image and scale compared to average size of marketMap logo..Faster

    for size in range(estimatedScaler-1, estimatedScaler+2):
        bestScore = 0
        size = float(size)
        sizex = size/10
        # print sizex

        # Perform tempate matching

        min_val, max_val, min_loc, max_loc, res, img = matchTheTemplate(marketMap, logo, sizex)

        # Keep track of highest score to try again at the end with smaller intervals
        if max_val > highest:
            highest = size

        # if score is greater than .8 then we have a match

        if isFound(max_val, img, res) == True:
            break

        # If score is greater than .6 recheck the size in smaller intervals

        if max_val > .6:
            try:
                # recheck takes current scale examle: scale=.4 and checks .35, .36, .37, .38... ,.4, .41, .42...
                min_val, max_val, min_loc, max_loc = recheck(logo, marketMap, sizex)
                if isFound(max_val, img, res) == True:
                    break
                else:
                    continue

            except:
                continue

    # If all fails then we try again with the highest score recorded
    if isFound(max_val, img, res) == False:
        try:
            # print "Doing last tests"
            sizex = float(highest)/10
            min_val, max_val, min_loc, max_loc = recheck(logo, marketMap, sizex)
            if max_val > .8:
                # plt.subplot(121),plt.imshow(res,cmap = 'gray')
                # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
                # plt.subplot(122),plt.imshow(img,cmap = 'gray')
                # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])

                return True

                # plt.suptitle(method)
                # plt.show()
        except:
            return False

    else:

        return True

