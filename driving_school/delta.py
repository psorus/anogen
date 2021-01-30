import numpy as np


def fromdelta(xx,yy):
  rx,ry=[],[]
  ax,ay=0.0,0.0
  for x,y in zip(xx,yy):
    ax+=x
    ay+=y
    rx.append(ax)
    ry.append(ay)
  return np.array(rx),np.array(ry)

def godelta(xx,yy):
  rx,ry=[xx[0]],[yy[0]]
  
  for i in range(1,len(xx)):
    rx.append(xx[i]-xx[i-1])
    ry.append(yy[i]-yy[i-1])
  return np.array(rx),np.array(ry)


if __name__=="__main__":
  x,y=np.random.random((2,10))
  print(x)
  print()
  # print(y)
  x,y=godelta(x,y)
  print(x)
  print()
  x,y=fromdelta(x,y)
  print(x)
  # print(y)




    