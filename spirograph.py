import pygame as pg
import math as m

def updatePoints(l, r, f):
    points = []
    for i in range(len(l)):
        if i == 0:
            points.append(
                    (
                        int(400+l[i]*m.cos(speed*m.pi*f*r[i]/(5*frameRate))),
                        int(400+l[i]*m.sin(speed*m.pi*f*r[i]/(5*frameRate)))
                    )
                )
        else:
            points.append(
                    (
                        int(l[i]*m.cos(speed*m.pi*f*r[i]/(5*frameRate))+points[i-1][0]),
                        int(l[i]*m.sin(speed*m.pi*f*r[i]/(5*frameRate))+points[i-1][1])
                    )
                )
    return points

lengths = [100,50]
rates = [1,2]
showLines = True
showCircle = True
fade = False
keep = False

#Create a pygame display object
d = pg.display.set_mode((800,800))

running = True
clock = pg.time.Clock()
frameRate = 360.0
speed = 10
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
    elif not keep:
        d.fill((10,10,10))
    for i in range(len(points)):
        if showLines:
            points.insert(0,(400,400))
            pg.draw.lines(d,(200,200,200),False,points)
        if showCircle:
            pg.draw.circle(d,(0,255,0),points[len(points)-1],1)
    pg.display.update()
    #Increment time by 1
    frame += 1
    #Wait for frame to end
    clock.tick(frameRate)
