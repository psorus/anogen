from xevo import eobj

import numpy as np


from helper import *


class boolflip(eobj):
  """trivial test eobj trying to maximize the sum of a list of 100 booleans. Also counts each call to calcstrength"""
  def __init__(s,q=None):
    s.initial()
    s.q=q
    if q is None:s.q=s.randomize().q
  def __str__(s):
    return "".join([str(qq) for qq in s.q])
  def __add__(a,b):
    ret=[]
    for aa,bb in zip(a.q,b.q):
      if np.random.randint(2)==0:
        ret.append(aa)
      else:
        ret.append(bb)
    return boolflip(ret)
  
  def randomize(s):
    ret=[]
    for i in range(28*28):
      ret.append(np.random.randint(2))
    return boolflip(ret)
  def mutate(s):
    rel=[p for p in s.q]
    i=np.random.randint(len(rel))
    rel[i]=1-rel[i]
    return boolflip(rel)
  def calcstrength(s):
    return float(lossbybool(s.q))
  def shallmaximize(s):return True
  def _copy(s):
    return boolflip([p for p in s.q])
