from xevo import erun,crossevo

from boolflip import *

obj=boolflip()
genetics=crossevo()#1120+-34


goalstrength=0.05
maxsteps=15000


def statinf(q):
  return {"shape":np.array(q).shape,"mean":np.mean(q),"std":np.std(q),"max":np.max(q),"min":np.min(q),"stdm":np.std(q)/np.sqrt(len(q))}

def runone(show=True):
  global c
  c=erun(genetics.copy(),obj,show=show,population=20)
  c.run(goalstrength=goalstrength,maxsteps=maxsteps)
  return 1

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



k=c.getwinner().q
plot(k)
plt.show()
for q in c.gettopn(n=3):
  plt.close()
  plot(q.q)
  plt.show()

# c.show_history(log=False)
