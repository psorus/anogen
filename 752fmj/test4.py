from xevo import erun,crossevo

from bitflip import *


obj=bitflip()
genetics=crossevo()#1120+-34


goalstrength=0.99
maxsteps=1000000


def statinf(q):
  return {"shape":np.array(q).shape,"mean":np.mean(q),"std":np.std(q),"max":np.max(q),"min":np.min(q),"stdm":np.std(q)/np.sqrt(len(q))}

def runone(show=True):
  counter.reset()
  global c
  c=erun(genetics.copy(),obj,show=show)
  c.run(goalstrength=goalstrength,maxsteps=maxsteps)
  return counter.i

# cc=[]
# for i in range(25):
  # cc.append(runone(False))
  # print(f"did {i}::{cc[-1]}")
# print(cc)
# print(statinf(cc))

runone(True)

print(c.getwinner())

print("top3 start")

for q in c.gettopn(n=3):
  print(q)

print("top3 end")
print(c.getwinner())



# c.show_history(log=False)
