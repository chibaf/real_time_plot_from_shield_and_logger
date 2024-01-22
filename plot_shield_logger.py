import ADS1256
from datetime import date
import time
import matplotlib.pyplot as plt
import serial

from read_m5_class import m5logger
from read_shield_class import Shield

today = date.today()
t=time.localtime()
current_time=time.strftime("_H%H_M%M_S%S",t)
fn="SL_"+str(today)+current_time+".csv"
f=open(fn,'w',encoding="utf-8")
start = time.time()

ldata0=[0]*10
ldata=[ldata0]*10
ser = serial.Serial("/dev/ttyUSB0",115200)
sport=m5logger()

data0=[0]*8
data=[data0]*10
data02=[0]*10
data2=[data02]*10
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
  array2=sport.read_logger(ser)
  f.write(st+ss[1:5]+","+str(rttime)+","
  +str(array[0])+","+str(array[1])+","+str(array[2])+","+str(array[3])+","+str(array[4])+","+str(array[5])+","+str(array[6])+","+str(array[7])+"," #20200122 added
  +str(array2[0])+","+str(array2[1])+","+str(array2[2])+","+str(array2[3])+","+str(array2[4])+","+str(array2[5])+","+str(array2[6])+","+str(array2[7])+","+str(array2[8])+","+str(array2[9])
  +"\n")
  print(st+ss[1:5]+","+str(rttime)+","
  +str(array[0])+","+str(array[1])+","+str(array[2])+","+str(array[3])+","+str(array[4])+","+str(array[5])+","+str(array[6])+","+str(array[7])+"," #20200122 added
  +str(array2[0])+","+str(array2[1])+","+str(array2[2])+","+str(array2[3])+","+str(array2[4])+","+str(array2[5])+","+str(array2[6])+","+str(array2[7])+","+str(array2[8])+","+str(array2[9]))
  data.pop(-1)
  data2.pop(-1)
  data.insert(0,array)
  data2.insert(0,array2)
  rez = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
  rez2 = [[data2[j][i] for j in range(len(data2))] for i in range(len(data2[0]))]
  x=range(0, 10, 1)
  plt.figure(100)
  plt.clf()
  plt.ylim(-1.0,5.0)
  lin0,=plt.plot(x,rez[0],label="A0")
  lin1,=plt.plot(x,rez[1],label="A1")
  lin2,=plt.plot(x,rez[2],label="A2")
  lin3,=plt.plot(x,rez[3],label="A3")
  lin4,=plt.plot(x,rez[4],label="A4")
  lin5,=plt.plot(x,rez[5],label="A5")
  lin6,=plt.plot(x,rez[6],label="A6")
  lin7,=plt.plot(x,rez[7],label="A7")
  plt.legend(handles=[lin0,lin1,lin2,lin3,lin4,lin5,lin6,lin7])
  plt.pause(0.1)
  plt.figure(200)
  plt.clf()
  plt.ylim(-25,30)
  tl0,=plt.plot(x,rez2[0],label="T0")
  tl1,=plt.plot(x,rez2[1],label="T1")
  tl2,=plt.plot(x,rez2[2],label="T2")
  tl3,=plt.plot(x,rez2[3],label="T3")
  tl4,=plt.plot(x,rez2[4],label="T4")
  tl5,=plt.plot(x,rez2[5],label="T5")
  tl6,=plt.plot(x,rez2[6],label="T6")
  tl7,=plt.plot(x,rez2[7],label="T7")
  tl8,=plt.plot(x,rez2[8],label="T8")
  tl9,=plt.plot(x,rez2[9],label="T9")
  plt.legend(handles=[tl0,tl1,tl2,tl3,tl4,tl5,tl6,tl7,tl8,tl9])
  plt.pause(0.1)
 except KeyboardInterrupt:
  f.close()
  ser.close()
  exit()
