import screenSizer
import random

vertex_list = []
filepath = "waveResize.jpg"

for i in range(50):
    vertex_list.append(((random.randint(0, screenSizer.getImgSize(filepath)[0]), random.randint(0, screenSizer.getImgSize(filepath)[1])),
                        (random.randint(0, screenSizer.getImgSize(filepath)[0]), random.randint(0, screenSizer.getImgSize(filepath)[1])),
                        (random.randint(0, screenSizer.getImgSize(filepath)[0]), random.randint(0, screenSizer.getImgSize(filepath)[1]))
                        ))      
    #vertex_list.append((random.randint(0,),0,0))

def grabRandomTriangle():
    thing = vertex_list[random.randint(0,50)]
    point_list = [thing[0][0], thing[0][1], thing[1][0], thing[1][1], thing[2][0], thing[2][1]]
    return point_list

#print(grabRandomTriangle())
