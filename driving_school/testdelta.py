import sys, pygame
import time
import numpy as np

from learnfrom import *
from motio import *
from delta import *

import matplotlib.pyplot as plt

pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
position=[20,20]
white=[255,255,255]

#plot from 0 to 1
def plot(x,y,pr,color="red"):
  for xx,yy,p in zip(x,y,pr):
    
    xx=(xx+1)/2
    yy=(yy+1)/2
    
    xx*=width
    yy*=height
    # xx-=width
    # yy-=height
    
    screen.fill(white)
    pygame.draw.circle(screen,color,[xx,yy],20,3)
    pygame.display.flip()
    print(xx,yy,p)
    pygame.time.wait(3)


phi=np.arange(0,100,dphi)
r=0.5
x=r*(np.cos(phi))
y=r*(np.sin(phi))

x=(phi/100-0.5)
y=x
y=y**2

plot(x[:1000],y[:1000],x[:1000],"blue")

par=understand(*godelta(x,y))
print("understood as",par)

# exit()

x2,y2,loss=loopfor(x[-1],y[-1],x[-2],y[-2],par,n=100)

x2,y2=fromdelta(x2,y2)



plot(x2,y2,loss,color="red")

plt.plot(x,y,".",color="red",alpha=0.5)
plt.plot(x2,y2,".",color="blue",alpha=0.5)
plt.show()

#need dx,dy


pygame.quit()