from motio import *
from learnfrom import *

import numpy as np
import matplotlib.pyplot as plt

par=[4.0,4.0,0.0,0.0]

x0=0.5
y0=0.0

print(funcbyparam(x0,y0,*par))
# exit()

x,y,loss=loopfor(x0,y0,x0,y0,par,n=4800)


x=np.array(x)
y=np.array(y)
loss=np.array(loss)

# print(x,y,loss)
print(x**2+y**2)


plt.plot(x,y,".",alpha=0.9)
plt.show()



