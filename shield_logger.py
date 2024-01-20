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
  +str(array[0])+","+str(array[1])+","+str(array[2])+","+str(array[3])+","+str(array[4])+","+str(array[5])+","+str(array[6])+","+str(array[7])
  +str(array2[0])+","+str(array2[1])+","+str(array2[2])+","+str(array2[3])+","+str(array2[4])+","+str(array2[5])+","+str(array2[6])+","+str(array2[7])+","+str(array2[8])+","+str(array2[9])
  +"\n")
  print(st+ss[1:5]+","+str(rttime)+","
  +str(array[0])+","+str(array[1])+","+str(array[2])+","+str(array[3])+","+str(array[4])+","+str(array[5])+","+str(array[6])+","+str(array[7])
  +str(array2[0])+","+str(array2[1])+","+str(array2[2])+","+str(array2[3])+","+str(array2[4])+","+str(array2[5])+","+str(array2[6])+","+str(array2[7])+","+str(array2[8])+","+str(array2[9]))
  data.pop(-1)
  data2.pop(-1)
  data.insert(0,array)
  data2.insert(0,array2)
  rez = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
  rez2 = [[data2[j][i] for j in range(len(data2))] for i in range(len(data2[0]))]
#  print(rez)
#  print(rez2)
 except KeyboardInterrupt:
  f.close()
  ser.close()
  exit()
