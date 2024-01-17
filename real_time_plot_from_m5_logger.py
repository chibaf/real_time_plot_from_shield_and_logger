import matplotlib.pyplot as plt
import serial
import sys

from read_m5_class import m5logger

data0=[0]*10
data=[data0]*10

ser = serial.Serial(sys.argv[2],sys.argv[1])
sport=m5logger()

while True:
  try:
    array=sport.read_logger(ser)
    if len(array)==10:
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
      plt.plot(x,rez[8])
      plt.plot(x,rez[9])
      plt.pause(0.1)
  except KeyboardInterrupt:
    print ('exiting')
    break
ser.close()
exit()