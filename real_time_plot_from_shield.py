import ADS1256
import time
import matplotlib.pyplot as plt

from read_shield_class import Shield

data0=[0]*8
data=[data0]*10
shield=Shield()
while True:
  try:
    array=shield.read_shield()
    if len(array)==8:
      data.pop(-1)
      data.insert(0,array)
      rez = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
      x=range(0, 10, 1)
      plt.clf()
      plt.plot(x,rez[0])
      plt.plot(x,rez[1])
      plt.plot(x,rez[2])
      plt.plot(x,rez[3])
      plt.plot(x,rez[4])
      plt.plot(x,rez[5])
      plt.plot(x,rez[6])
      plt.plot(x,rez[7])
      plt.pause(0.1)
  except KeyboardInterrupt:
    print ('exiting')
    break
exit()