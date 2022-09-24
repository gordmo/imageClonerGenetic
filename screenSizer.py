from PIL import Image



def getImgSize(filepath):
    img = Image.open(filepath)
    return img.size