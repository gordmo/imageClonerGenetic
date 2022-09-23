import sys, pygame
from PIL import Image

filepath = "waveResize.jpg"

def getImgSize(filepath):
    img = Image.open(filepath)
    return img.size

pygame.init()

size = getImgSize(filepath)
black = 0, 0, 0

screen = pygame.display.set_mode(size)

wave = pygame.image.load(filepath)
waveRect = wave.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    

    screen.fill(black)
    screen.blit(wave, waveRect)
    pygame.display.flip()
