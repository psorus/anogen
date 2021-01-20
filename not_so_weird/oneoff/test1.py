import numpy as np
import matplotlib.pyplot as plt
from simplestat import statinf

f=np.load("model.npz",allow_pickle=True)

model=f["model"]
t=f["t"]
at=f["at"]

print(*[m.shape for m in model])
print(t.shape)
# exit()


def runmodel(inp):
  x=inp
  for l in model:
    x=np.dot(x,l)
    x=np.maximum(x,0)
  x=np.mean(x,axis=-1)
  return x

print("doing 7")
to=runmodel(t)
print("doing ~7")
ato=runmodel(at)
print("done")

print(statinf(to))
print(statinf(ato))
# exit()

plt.hist(to,bins=50,alpha=0.5,label="7")
plt.hist(ato,bins=50,alpha=0.5,label="~7")

plt.legend()
plt.show()
