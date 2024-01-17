import ADS1256
from datetime import date
import time
import matplotlib.pyplot as plt

from read_shield_class import Shield

today = date.today()
t=time.localtime()
current_time=time.strftime("_H%H_M%M_S%S",t)
fn="SH_"+str(today)+current_time+".csv"
f=open(fn,'w',encoding="utf-8")
start = time.time()

data0=[0]*8
data=[data0]*10
shield=Shield()
while True:
  try:
    ttime=time.time()-start
    if ttime<0.001:
      ttime=0.0
    st=time.strftime("%Y %b %d %H:%M:%S", time.localtime())
    ss=str(time.time()-int(time.time()))
    rttime=round(ttime,2)

    array=shield.read_shield()
    if len(array)==8:
      data.pop(-1)
      data.insert(0,array)
      rez = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
      f.write(st+ss[1:5]+","+str(rttime)+","+str(array[0])+","+str(array[1])+","+str(array[2])+str(array[3])+","+str(array[4])+","+str(array[5])+str(array[6])+","+str(array[7])+"\n")
      x=range(0, 10, 1)
      plt.clf()
      lin0,=plt.plot(x,rez[0],label="L0")
      lin1,=plt.plot(x,rez[1],label="L1")
      lin2,=plt.plot(x,rez[2],label="L2")
      lin3,=plt.plot(x,rez[3],label="L3")
      lin4,=plt.plot(x,rez[4],label="L4")
      lin5,=plt.plot(x,rez[5],label="L5")
      lin6,=plt.plot(x,rez[6],label="L6")
      lin7,=plt.plot(x,rez[7],label="L7")
      plt.legend(handles=[lin0,lin1,lin2,lin3,lin4,lin5,lin6,lin7])
      plt.pause(0.1)
  except KeyboardInterrupt:
    print ('exiting')
    break
exit()