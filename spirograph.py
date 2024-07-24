import pygame as pg
import math as m

def updatePoints(l, r, f):
    points = []
    for i in range(len(l)):
        if i == 0:
            points.append(
                    (
                        int(400+l[i]*m.cos(m.pi*f*r[i]/100)),
                        int(400+l[i]*m.sin(m.pi*f*r[i]/100))
                    )
                )
        else:
            points.append(
                    (
                        int(l[i]*m.cos(m.pi*f*r[i]/100)+points[i-1][0]),
                        int(l[i]*m.sin(m.pi*f*r[i]/100)+points[i-1][1])
                    )
                )
    return points

lengths = [100,100,100,100]
rates = [2,-3,5,-7]
showLines = True
fade = False

#Create a pygame display object
d = pg.display.set_mode((800,800))

running = True
clock = pg.time.Clock()
frameRate = 120.0
frame = 0
d.fill((10,10,10))
print(len(updatePoints(lengths,rates,0)))
while running:
    #Check for quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    #Calculate points
    points = updatePoints(lengths,rates,frame)
    #Update display
    if fade:
        d.fill((10,10,10),special_flags=2)
    for i in range(len(points)):
        if showLines:
            points.insert(0,(400,400))
            pg.draw.lines(d,(255,255,255),False,points)
        else:
            pg.draw.circle(d,(255,255,255),points[len(points)-1],3)
    pg.display.update()
    #Increment time by 1
    frame += 1
    #Wait for frame to end
    clock.tick(frameRate)
