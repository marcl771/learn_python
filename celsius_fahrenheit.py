# Celsius Fahrenheit umrechner

print("Temperaturumrechner".center(100))
print("[1] Celsius zu Fahrenheit | [2] Fahrenheit zu Celsius".center(100))
auswahl = int(input("Auswahl: "))

if auswahl == 1:
    tempc = int(input("Temperatur in °C: "))
    tempf = tempc*1.8+32
    print(tempf, "°F")
elif auswahl == 2:
    tempf = int(input("Temperatur in °F: "))
    tempc1 = (tempf - 32)*0.555
    tempc2 = str(tempc1)
    print(tempc2.replace(".",","), "°C")
else:
    print("Eingabe nicht erkannt")
