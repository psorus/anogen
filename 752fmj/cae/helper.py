import matplotlib.pyplot as plt
import numpy as np



def plot(ac):
  ac=np.array(ac)
  ac=ac.reshape((28,28))
  ac=[[int(ac2) for ac2 in ac1] for ac1 in ac]


  plt.imshow(ac)

