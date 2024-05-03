from machine import Pin
from mfrc522 import MFRC522
import utime
from machine import I2C, Pin
import ssd1306
import time
import framebuf
import network
import socket
from time import sleep
import machine






i2c = I2C(0, scl=Pin(1), sda=Pin(0))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
       
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=6)

 
print("Bring RFID TAG Closer...")
print("")





while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            
            if card == 3654636243:
                print("Card ID: "+ str(card)+" Recognised as D352, displaying boinger.")
                images = []
                for n in range(1,7):
                    with open('Boing.%s.pbm' % n, 'rb') as f:
                        f.readline() # Magic number
                        f.readline() # Creator comment
                        f.readline() # Dimensions
                        data = bytearray(f.read())
                    fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
                    images.append(fbuf)
                
            
                display.invert(1)
                while True:
                    for i in images:
                        display.blit(i, 0, 0)
                        display.show()
                        time.sleep(0.1)
                    break

                
            elif card == 3668458387:
                print("Card ID: "+ str(card)+" Recognised as 933B, displaying Isaac.")
                images = []
                for n in range(1,8):
                    with open('izek.%s.pbm' % n, 'rb') as f:
                        f.readline() # Magic number
                        f.readline() # Creator comment
                        f.readline() # Dimensions
                        data = bytearray(f.read())
                    fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
                    images.append(fbuf)
                
                display.invert(1)
                while True:
                    for i in images:
                        display.blit(i, 0, 0)
                        display.show()
                        time.sleep(0.1)
                    break
                
            else:
                print("Card ID: "+ str(card)+" UNKNOWN CARD! Kakis deploed!")
                with open('kakis.pbm', 'rb') as f:
                    f.readline() # Magic number
                    f.readline() # Creator comment
                    f.readline() # Dimensions
                    data = bytearray(f.read())
                fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

            display.invert(1)
            display.invert(1)
            display.blit(fbuf, 0, 0)
            display.show()
            


