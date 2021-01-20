import matplotlib.pyplot as plt
import numpy as np



def plot(ac):
  ac=np.array(ac)
  ac=ac.reshape((28,28))
  ac=[[int(ac2+0.48) for ac2 in ac1] for ac1 in ac]


  plt.imshow(ac)

f=np.load("model.npz",allow_pickle=True)
f2=np.load("model2.npz",allow_pickle=True)
f3=np.load("model3.npz",allow_pickle=True)
f4=np.load("model4.npz",allow_pickle=True)
f5=np.load("model5.npz",allow_pickle=True)

model=f["model"]
print("exp model1")
model2=f2["model"]
print("exp model2")
model3=f3["model"]
print("exp model3")
model4=f4["model"]
print("exp model4")
model5=f5["model"]
print("exp model5")

models=[model,model2,model3,model4,model5]
t=f["t"]
t0=np.mean(t[np.where(t<0.5)])
t1=np.mean(t[np.where(t>0.5)])

def runmodel(inp,model):
  x=inp
  for l in model:
    x=np.dot(x,l)
    x=np.maximum(x,0)
  x=np.mean(x,axis=-1)
  return x

def lossbybool(inp):
  """input either 0 or 1"""
  dt=t1-t0
  inp/=dt
  inp+=t0
  ret=(runmodel(inp,models[0])-m7[0])**2
  for zw,mea in zip(models[1:],m7):
    ret+=(runmodel(inp,models[0])-mea)**2
  return ret/len(m7)

m7=[np.mean(runmodel(t,m)) for m in models]


print("done loading")

