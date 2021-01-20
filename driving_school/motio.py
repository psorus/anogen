from learnfrom import *
import numpy as np
from tqdm import tqdm

dphi=0.01
dr=0.01

def findbestnext(x0,y0,xm1,ym1,p):
  phi=np.arange(np.random.random()*dphi,2*np.pi,dphi)
  x=[x0+dr*np.sin(p) for p in phi]
  y=[y0+dr*np.cos(p) for p in phi]
  val=[lossbyparam(xx,yy,*p) for xx,yy in zip(x,y)]
  q=[]
  # q=val
  drsq=dr**2
  for zw,xx,yy in zip(val,x,y):
    dra=(xx-xm1)**2+(yy-ym1)**2
    if dra<drsq/3:
      zw+=100#move in the same direction
    # zw-=dra*0.1
    q.append(zw)
  i=np.argmin(q)
  # print("minidex",i,len(x),len(y),len(q),len(phi))
  return x[i],y[i],q[i]


def loopfor(x0,y0,xm1,ym1,p,n=10000):
  x=[xm1,x0]
  y=[ym1,y0]
  loss=[-1,-1]
  
  for i in tqdm(range(n)):
    ax,ay,al=findbestnext(x[-1],y[-1],x[-2],y[-2],p)
    x.append(ax)
    y.append(ay)
    loss.append(al)
  return x,y,loss
  
  
  


  
  




