class m5logger:
    
  def read_logger(self,ser):
    import serial
    line = ser.readline()
    try:
      line2=line.strip().decode('utf-8')
    except UnicodeDecodeError:
      return [0.0]*10
    data = [str(val) for val in line2.split(",")]
    data1=[]
    if len(data)==12:
      for i in range(0,10):
        try:
          fd=float(data[i+2])
        except:
          return [0.0]*10
        data1.append(fd)
    else:
      return [0.0]*10
    return data1