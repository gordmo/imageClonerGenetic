import screenSizer
import random
import numpy as np
from PIL import Image

poly_List = []
color_list = []
filepath = "waveResize.jpg"

for i in range(50):
    poly_List.append(((random.randint(0, screenSizer.getImgSize(filepath)[0]), random.randint(0, screenSizer.getImgSize(filepath)[1])),
                        (random.randint(0, screenSizer.getImgSize(filepath)[0]), random.randint(0, screenSizer.getImgSize(filepath)[1])),
                        (random.randint(0, screenSizer.getImgSize(filepath)[0]), random.randint(0, screenSizer.getImgSize(filepath)[1])),
                        (random.randint(0, screenSizer.getImgSize(filepath)[0]), random.randint(0, screenSizer.getImgSize(filepath)[1])),
                        #color tuple
                        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                        ))  

def getPoly(poly):
    points = [[poly[0][0], poly[0][1], poly[1][0], poly[1][1], poly[2][0], poly[2][1], poly[3][0], poly[3][1]],(poly[4][0], poly[4][1], poly[4][2])]
    return points

def getPolyList():
    return poly_List

def genRandomPoly():
    return poly_List[random.randint(0,49)]

def grabRandomPoly():
    thing = genRandomPoly()
    points = [[thing[0][0], thing[0][1], thing[1][0], thing[1][1], thing[2][0], thing[2][1], thing[3][0], thing[3][1]],(thing[4][0], thing[4][1], thing[4][2])]
    return points

def genColor():
    poly = genRandomPoly()
    return ((poly[4][0], poly[4][1], poly[4][2]))

optimal = np.asarray(Image.open(filepath), dtype = int)
def fitness():
    generated_IMG = np.asarray(Image.open("screenshot.png"), dtype = int)
    return np.sqrt(((optimal - generated_IMG)**2).sum(axis=-1)).sum()
