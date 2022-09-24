import pyglet
import pyglet.window.key
from pyglet import shapes
import random
from PIL import Image
import genAlgo

filepath = "waveResize.jpg"

def getImgSize(filepath):
    img = Image.open(filepath)
    return img.size

window = pyglet.window.Window(getImgSize(filepath)[0], getImgSize(filepath)[1], "Original Image")
image = pyglet.resource.image(filepath)

window2 = pyglet.window.Window(getImgSize(filepath)[0], getImgSize(filepath)[1], "Geneticly Cloned Image")
main_Batch = pyglet.graphics.Batch()

point_list = [59, 149, 328, 204, 305, 284, 3, 197] #, 25, 107, 18, 61
ec = int(len(point_list)/2)
main_Batch.add(ec, pyglet.gl.GL_TRIANGLE_FAN, None, 
    ("v2i", genAlgo.grabRandomTriangle()), #genAlgo.grabRandomTriangle()
    ("c3B", (255, 0, 0) * ec))



@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

@window2.event
def on_draw():
    window2.clear()
    main_Batch.draw()


# key press event    
@window.event
def on_key_press(symbol, modifier):
    # key "C" get press
    if symbol == pyglet.window.key.ESCAPE:
        # close the window
        window.close()
        # window2.close()


#window.set_location(100, 400)
#window2.set_location(1300, 400)

pyglet.app.run()