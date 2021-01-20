from helper import *
import numpy as np
from simplestat import sprint
n=100


x=np.random.randint(0,2,(n,28*28,)).astype("float")

l=lossbybool(x)

sprint(l)

exit()


plot(x)
plt.title(str(lossbybool(x)))
plt.show()






