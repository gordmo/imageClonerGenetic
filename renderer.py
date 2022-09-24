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

#window = pyglet.window.Window(getImgSize(filepath)[0], getImgSize(filepath)[1], "Original Image")
image = pyglet.resource.image(filepath)

window2 = pyglet.window.Window(getImgSize(filepath)[0], getImgSize(filepath)[1], "Geneticly Cloned Image")
main_Batch = pyglet.graphics.Batch()

#ec = int(len(point_list)/2)

for poly in genAlgo.getPolyList():
    poly = genAlgo.getPoly(poly)
    ec = int(len(poly[0])/2)
    main_Batch.add(ec, pyglet.gl.GL_TRIANGLE_FAN, None, 
                    ("v2i", poly[0]), #genAlgo.grabRandomPoly()
                    ("c3B", poly[1] * ec)) #genAlgo.genColor()

@window2.event
def on_draw():
    window2.clear()
    main_Batch.draw()
    pyglet.image.get_buffer_manager().get_color_buffer().save('screenshot.png')

# key press event    
@window2.event
def on_key_press(symbol, modifier):
    # key "C" get press
    if symbol == pyglet.window.key.ESCAPE:
        # close the window
        window2.close()
        # window2.close()

#window.set_location(100, 400)
#window2.set_location(1300, 400)

pyglet.app.run()