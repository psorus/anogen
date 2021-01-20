from keras.layers import Conv2D
from keras.layers import Input
from keras.layers import MaxPooling2D, UpSampling2D
from keras.models import Model
from keras.datasets.mnist import load_data
from numpy import reshape
import matplotlib.pyplot as plt


from keras.models import load_model
import numpy as np


model = load_model('model.hdf5')

f=np.load("data.npz")
x=f["x"]
# print(x.shape)
# exit()


def evaluate(q):
  q=np.array(q)
  p=model.predict(np.reshape(q,(int(np.prod(q.shape)/(28*28)),28,28)),verbose=0)
  return np.sqrt(np.mean((p-q)**2))


