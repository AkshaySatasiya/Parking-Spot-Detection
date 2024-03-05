import pickle

from skimage.transform import resize
import numpy as np
import cv2


EMPTY = True
NOT_EMPTY = False

MODEL = pickle.load(open("model.p", "rb"))

def empty_or_not(spot_bgr):

    flat_data = []

    image_resized = resize(spot_bgr, (15,15,3))
    flat_data.append(image_resized.flatten())
    flat_data = np.array(flat_data)

    y_output = MODEL.predict(flat_data)

    if y_output == 0:
        return EMPTY
    else: 
        return NOT_EMPTY


def get_parking_spot_bboxes(connected_components):
    (totalLabels, label_ids, values, centroid) = connected_components

    slot = []
    coef = 1

    for i in range(1, totalLabels):
        #Extracting coordinate points
        x1 = int(values[i, cv2.CC_STAT_LEFT]*coef)
        y1 = int(values[i, cv2.CC_STAT_TOP]*coef)
        w = int(values[i, cv2.CC_STAT_WIDTH]*coef)
        h = int(values[i, cv2.CC_STAT_HEIGHT]*coef)

        slot.append([x1,y1,w,h])

    return slot