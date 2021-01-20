import numpy as np
import json

from ageta import *


vae,encoder,decoder=getvaeq()


def clean(q):
  if type(q) is dict:
    for key in q.keys():
      q[key]=clean(q[key])
    return q
  if type(q) is list:
    for i in range(len(q)):
      q[i]=clean(q[i])
    return q
  return str(q) 

def traf(q):
  ll=q.layers
  ret=[]
  for l in ll:

    c=l.get_config()
    
    c.update({"type":str(type(l))})

    c=clean(c)

    ret.append(c)
  return ret


with open("model.json","w") as f:
  f.write(json.dumps({"encoder":traf(encoder),"decoder":traf(decoder)},indent=2))




