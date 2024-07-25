import math as m
import cmath as cm
import pygame as pg

width = 400
height = 240

disp = pg.display.set_mode((width,height))

running = True
clock = pg.time.Clock()
frameRate = 6000.0
frame = 0

depth = 5
disp.fill((128,128,128))
while running:
    #Check for quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    posX = frame%width-(3*width/4)
    posY = m.floor(frame/width)-(height/2)
    a = posX/100.0
    b = posY/100.0
    z = [0]
    c = complex(a,b)
    color = (255,255,255)
    for i in range(depth):
        z.append(z[i]**2+c)
        for j in range(i):
            if cm.isclose(z[i+1],z[j],rel_tol=0.1):
                color = (0,0,0)
                

    #Update display
    disp.set_at((int(posX+(3*width/4)),int(posY+(height/2))),color)
    pg.display.update()
    
    #Increment frame by 1
    if frame < width*height:
        frame += 1
    #Wait for frame to end
    clock.tick(frameRate)
