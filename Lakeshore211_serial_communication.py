#!/usr/bin/env python
# coding: utf-8

# In[1]:


import serial 
import time


# In[ ]:


COMPort = "COM7" #replace COM port depends on your settings

ser = serial.Serial(COMPort,baudrate = 9600,timeout = 1, stopbits = serial.STOPBITS_ONE, 
                    parity = serial.PARITY_ODD, bytesize = serial.SEVENBITS )
try:
    #ask IDN
    ser.write(b"*IDN?\r\n")
    t = ser.readline().decode()
    print (t)
    time.sleep(0.1)
    #return should be
    #LSCI,MODEL211,21A0000,022607


    #Get Temperature (K unit)
    ser.write(b"KRDG?\r\n")
    t = ser.readline().decode()
    print (f"Temp:{float(t)} K ")
    time.sleep(0.1)

    #Get Temperature (Celsius unit)
    ser.write(b"CRDG?\r\n")
    t = ser.readline().decode()
    print (f"Temp:{float(t)} K ")
    time.sleep(0.1)
except Exception as e:
    print (e)

finally:
    ser.close()

