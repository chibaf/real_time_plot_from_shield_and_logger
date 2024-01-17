import serial, sys

strPort = sys.argv[1]
ser=serial.Serial(strPort, sys.argv[2])
print("connected to: " + ser.portstr)

while True:
  line = ser.readline()
  print(line)
