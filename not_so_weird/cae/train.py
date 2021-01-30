from keras.layers import Conv2D
from keras.layers import Input
from keras.layers import MaxPooling2D, UpSampling2D
from keras.models import Model
from keras.datasets.mnist import load_data
from numpy import reshape
import matplotlib.pyplot as plt
from keras.callbacks import ModelCheckpoint
import numpy as np

(xtrain0, ytrain0), (xtest0, ytest0) = load_data()

def wheredex(x,y,d=7):
  assert len(x)==len(y),f"{len(x)} {len(y)}"
  i=np.where(y==d)
  k=x[i]
  if len(k)>5000:k=k[:5000]
  return reshape(k.astype('float32') / 255, (len(k), 28, 28, 1))#[:5000]
def wherenotdex(x,y,d=7):
  assert len(x)==len(y),f"{len(x)} {len(y)}"
  i=np.where(y!=d)
  k=x[i]
  if len(k)>5000:k=k[:5000]
  return reshape(k.astype('float32') / 255, (len(k), 28, 28, 1))#[:5000]


xtrain=wheredex(xtrain0,ytrain0,7)
xatrain=wherenotdex(xtrain0,ytrain0,7)
xtest=wheredex(xtest0,ytest0,7)
xatest=wherenotdex(xtest0,ytest0,7)


np.savez_compressed("data",x=xtrain,xa=xatrain,xval=xtest,xaval=xatest)


print(xtrain.shape, xtest.shape) 


input_img = Input(shape=(28, 28, 1))

enc_conv1 = Conv2D(12, (3, 3), activation='relu', padding='same')(input_img)
enc_pool1 = MaxPooling2D((2, 2), padding='same')(enc_conv1)
enc_conv2 = Conv2D(8, (4, 4), activation='relu', padding='same')(enc_pool1)
enc_ouput = MaxPooling2D((4, 4), padding='same')(enc_conv2)

dec_conv2 = Conv2D(8, (4, 4), activation='relu', padding='same')(enc_ouput)
dec_upsample2 = UpSampling2D((4, 4))(dec_conv2)
dec_conv3 = Conv2D(12, (3, 3), activation='relu')(dec_upsample2)
dec_upsample3 = UpSampling2D((2, 2))(dec_conv3)
dec_output = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(dec_upsample3)

autoencoder = Model(input_img, dec_output)
autoencoder.compile(optimizer='rmsprop', loss='binary_crossentropy')
autoencoder.summary()
 


checkpoint = ModelCheckpoint("model.hdf5", monitor='loss', verbose=1,
    save_best_only=True, mode='auto', period=1)
 
autoencoder.fit(xtrain, xtrain, epochs=20, batch_size=128, shuffle=True,callbacks=[checkpoint])

decoded_imgs = autoencoder.predict(x_test)

n = 10
plt.figure(figsize=(20, 4))
for i in range(n):
  plt.gray()
  ax = plt.subplot(2, n, i+1)
  plt.imshow(x_test[i].reshape(28, 28))
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
 
  ax = plt.subplot(2, n, i +1+n)
  plt.imshow(decoded_imgs[i].reshape(28, 28))
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
plt.show()