from read_shield_class import Shield
import time
import ADS1256

shield=Shield()
while True:
  adcv=shield.read_shield()
  print(adcv)
  time.sleep(0.5)
exit()
