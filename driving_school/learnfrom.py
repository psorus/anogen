
from scipy.optimize import minimize as mini

import numpy as np


#all of type a*x**2+b*y**2+c*x+d*y


def funcbyparam(x,y,a,b,c,d):
  return a*x**2+b*y**2+c*x+d*y

def lossbyparam(x,y,a,b,c,d):
  return (funcbyparam(x,y,a,b,c,d)-1)**2

def loss(p,x,y):
  loss=lossbyparam(x,y,*p)
  loss=np.mean(loss)
  return loss


def understand(x,y):
  print("learning structure")
  return mini(loss,[0.25 for i in range(4)],args=(x,y)).x


if __name__=="__main__":
  phi=np.arange(0,100,0.01)
  r=0.5
  x=r*(np.cos(phi))
  y=r*(np.sin(phi))
  
  
  print(understand(x,y))





