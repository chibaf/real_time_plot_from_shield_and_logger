class Shield:

  def __init__(self):
    import ADS1256
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()

  def read_shield(self):

    import RPi.GPIO as GPIO
    import ADS1256

    ADC = ADS1256.ADS1256()
    adcv=[]
    ADC_Value = ADC.ADS1256_GetAll()

    for i in range(8):
      adcv.append(ADC_Value[i]*5.0/0x7fffff)

#    GPIO.cleanup()
    return adcv
