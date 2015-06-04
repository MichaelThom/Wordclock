# Funktionen importieren
import Matrix
import clock
import time

clockList = [clock.esIst, clock.fuenf, clock.zehn, clock.zwanzig, clock.drei, clock.viertel, clock.vor, clock.nach, clock.halb, clock.hEins, clock.hZwei, clock.hDrei, $
clockListMinute = [clock.fuenf, clock.zehn, clock.zwanzig, clock.drei, clock.viertel, clock.vor, clock.nach, clock.halb] #0-7
clockListHour = [clock.hEins, clock.hZwei, clock.hDrei, clock.hVier,clock.hFuenf, clock.hSechs, clock.hSieben, clock.hAcht, clock.hNeun, clock.hZehn,clock.hElf, clock.$
clockListAdd = [clock.esIst, clock.uhr]
# Eine huebsche Startanimation
for m in clockList:
        table= [[ 0 for g in range(32) ] for h in range(32)]
        m(table)
        x = 0
        while x <= 5:
                Matrix.panel(table)
                x=x+1

### ab hier gehts richtig los
# einfache Endlosschleife Ostdeutsche System
while True:
        # lokale Zeit im RPi erfassen
        zeit = time.localtime()
        #Variablen fuer Stunden, minuten, sekunden setzen
        hour = time.strftime("%I", zeit)
        minute = time.strftime("%M", zeit)
        second = time.strftime("%S", zeit)
        #Das ganze als Integer zur Verfuegung stellen
        hour = int(hour)
        minute = int(minute)
        second = int(second)
        #leere Tabelle erstellen
        table= [[ 0 for g in range(32) ] for h in range(32)]
        # Es ist leuchtet immer
        clockListAdd[0](table)
        # Trennung zwischen gesprochenen Stunden Ausnahme ist hier Viertel
        if minute < 15 :
                clockListHour[hour-1](table)
                if minute < 5:
                        clockListAdd[1](table)
                elif (5 <= minute < 10):
                        clockListMinute[0](table)
                        clockListMinute[6](table)
                else:
                        clockListMinute[1](table)
                        clockListMinute[6](table)

        if (15 <= minute < 20):
                clockListHour[hour](table)
                clockListMinute[4](table)

        if (20 <= minute < 25):
                clockListHour[hour-1](table)
                clockListMinute[2](table)
                clockListMinute[6](table)

        if (25 <= minute < 45):
                clockListHour[hour](table)
                clockListMinute[7](table)

                if (25 <= minute < 30):
                        clockListMinute[0](table)
                        clockListMinute[5](table)

                elif (35 <= minute < 40):
                        clockListMinute[0](table)
                        clockListMinute[6](table)

                elif (40 <= minute < 45):
                        clockListMinute[1](table)
                        clockListMinute[6](table)


        if (45 <= minute < 50):
                clockListHour[hour](table)
                clockListMinute[3](table)
                clockListMinute[4](table)

        if (50 <= minute < 55):
                clockListHour[hour](table)
                clockListMinute[1](table)
                clockListMinute[5](table)

        if (55 <= minute <= 59):
                clockListHour[hour](table)
                clockListMinute[0](table)
                clockListMinute[5](table)

        for n in range(30-second, 30):
                table[n-2][2] = 1
        if (30 <= second <= 60):
                for n in range(second-30):
                        table[n][29] = 1


        Matrix.panel(table)


