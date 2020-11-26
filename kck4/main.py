import cv2
import math
import os
import numpy as np
dirimg = ['1g','2g','5g','10g','20g','50g','1z','2z','5z']
template = '1z/1.png'
def histogram(image_o):
    image = cv2.imread(image_o)  # image
    image = cv2.Canny(image, 255 / 3, 255)
    h = image.shape[0]
    w = image.shape[1]
    first = 0
    second = 0
    third = 0
    fourth = 0
    r=w/2+h/2
    r=r/2
    pixel_count=(w/2)*(h/2)-((w*h)-(math.pi*((r/2)**2)))/4

    # print(pixel_count/((w/2)*(h/2)))
    # int(round(w / 2))
    for y in range(0, int(round(h / 2))):
        for x in range(0, int(round(w / 2))):
            if image[y, x] != 0:
                third = third + 1
    for y in range(int(round(h / 2)), h):
        for x in range(0, int(round(w / 2))):
            if image[y, x] != 0:
                second = second + 1
    for y in range(0, int(round(h / 2))):
        for x in range(int(round(h / 2)), w):
            if image[y, x] != 0:
                fourth = fourth + 1
    for y in range(int(round(h / 2)), h):
        for x in range(int(round(w / 2)), w):
            if image[y, x] != 0:
                first = first + 1
    array=[first/pixel_count, second/pixel_count, third/pixel_count, fourth/pixel_count]
    # print(first, second, third, fourth, array)
    return array

def similarity(array1,array2):
    first = abs(array1[0] - array2[0])
    second =abs(array1[1] - array2[1])
    third =abs(array1[2] - array2[2])
    fourth =abs(array1[3] - array2[3])
    # print(1-math.sqrt((first**2 + second**2 + third**2 + fourth**2) / 4))
    return(1-math.sqrt((first**2 + second**2 + third**2 + fourth**2) / 4))

# image = cv2.imread('1g/1.png')  # image
# image = cv2.Canny(image, 255 / 3, 255)
similar_value=[]
similar=[]
for direct in dirimg:
    sim = []
    for filename in os.listdir(direct):
        if filename.endswith(".png"):
            sim.append(similarity(histogram(template),histogram(os.path.join(direct,filename))))
    for i in range (0,3):
        sim.append(np.max(sim))
    for i in range(0, 3):
        sim.append(np.max(sim))
    similar_value.append(np.mean(sim))
    similar.append(direct)
print(similar[similar_value.index(np.max(similar_value))])



