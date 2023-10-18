import pandas as pd
import numpy as np

def interpolacao(y1, y2, x1, x2, xa):
  if((float(y2) - float(y1)) == 0 or (float(x2) - float(x1)) == 0):
      return None
  else:
    result = (((float(y2) - float(y1)) / (float(x2) - float(x1))) * (float(xa) - float(x1)) + float(y1))
    return round(result, 2)

ab = pd.read_csv("./abalone.csv",header=None)
ind = np.random.rand(4178) >= 0.9
ab.iloc[ind,2]=None

imax,_=ab.shape

x = []
y = []

for i in range(imax):
  if i > 0:
    x.append(ab.iloc[i,1])
    y.append(ab.iloc[i,2])

for k in range(len(y)-1):
  print(y[k])
  if(k > 1 and y[k] == None):
    if((y[k-1] != None) and y[k+1] != None):
      y[k] = interpolacao(y[k-1], y[k+1], x[k-1], x[k+1], x[k])
