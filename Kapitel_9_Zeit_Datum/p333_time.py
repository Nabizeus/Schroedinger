from datetime import time

zeit = time(hour=3,minute=11,second=4)



print(zeit.strftime("Uhrzeit %HH:%MM:%SS"))
print(zeit.strftime("Uhrzeit %H:%M:%S"))


#Auf Zeitobjekt via .hour, .minute, .second zugreifen
print("zeit.hour ",zeit.hour)
print("zeit.minute ",zeit.minute)
print("zeit.second ",zeit.second)

# Zeiten aendern

print(" zeit.replace(7,34)",zeit.replace(7,34))