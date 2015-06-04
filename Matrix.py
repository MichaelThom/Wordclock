# Datei MUSS Matrix.py genannt werden oder im wordclock programm angepasst werden
#Gpio importieren
import RPi.GPIO as GPIO
import time

# use P1 header pin numbering convention
GPIO.setmode(GPIO.BOARD)
# Bereits gesetzte Gpio warnung deaktivieren
GPIO.setwarnings(False)

#Pins als Variablen setzen Bei Veraenderung der Pinkonfiguration anpassen
redZero = 11
greenZero = 12
blueZero = 15
redOne = 16
greenOne = 18
blueOne = 22
a = 26
b = 24
c = 21
d = 19
oe = 13
clock = 23
latch = 7

# GPIO Pin - als output
GPIO.setup(redZero, GPIO.OUT)
GPIO.setup(greenZero, GPIO.OUT)
GPIO.setup(blueZero, GPIO.OUT)
GPIO.setup(redOne, GPIO.OUT)
GPIO.setup(greenOne, GPIO.OUT)
GPIO.setup(blueOne, GPIO.OUT)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(oe, GPIO.OUT)
GPIO.setup(clock, GPIO.OUT)
GPIO.setup(latch, GPIO.OUT)

# GPIOListe (array)
gpioList = [oe, d, c, b, a]
Zero = [redZero, greenZero, blueZero]
One = [redOne, greenOne, blueOne]

def panel(table):
        for j in range(16):
# bin wandelt j in binaer Zahl um, zfill fuellt auf 5 Stellen auf (oe muss mit), 2: kuerzt die ersten beiden Stellen (0b),list erstellt eine Liste
                demux = list(bin(j)[2:].zfill(5))
# steuert den Demultiplexer an
                for x in range(5):
                        if demux[x] == '0':
                                GPIO.output(gpioList[x], False)
                        elif demux[x] == '1':
                                GPIO.output(gpioList[x], True)
                for i in range(32):
                        if table [j][i] == 0:
                                GPIO.output(clock, GPIO.HIGH)
                                GPIO.output(clock, GPIO.LOW)
                        elif table [j][i] == 1:
                                for a in range(3):
                                        GPIO.output(Zero[a], GPIO.HIGH)
                                GPIO.output(clock, GPIO.HIGH)
                                GPIO.output(clock, GPIO.LOW)
                                for a in range(3):
                                        GPIO.output(Zero[a], GPIO.LOW)
                GPIO.output(latch, GPIO.HIGH)
                GPIO.output(latch, GPIO.LOW)

                for i in range(32):
                        if table [j+16][i] == 0:
                                GPIO.output(clock, GPIO.HIGH)
                                GPIO.output(clock, GPIO.LOW)
                        elif table [j+16][i] == 1:
                                for a in range(3):
                                        GPIO.output(One[a], GPIO.HIGH)
                                GPIO.output(clock, GPIO.HIGH)
                                GPIO.output(clock, GPIO.LOW)
                                for a in range(3):
                                        GPIO.output(One[a], GPIO.LOW)

                GPIO.output(latch, GPIO.HIGH)
                GPIO.output(latch, GPIO.LOW)

