import math

""" Dieses Modul stellt dir Funktionen zur Verfuegung, mit denen auch komplizierte Rechnungen durchgefuert werden"""

aufgerundet = math.ceil
abgerundet = math.floor
print(aufgerundet(41.8))
print(abgerundet(14.2))
print(math.sin(math.radians(90)))
print(math.tan(math.radians(90)))
print(math.sin(1.5334))
print(math.tan(1.5334))

# random

import random

zufallszahl = random.random()
print("Zufallszahl 0-1: ",zufallszahl)

# randint
zufallszahl = random.randint(1,49)
print("Randint Zufallszahl 1-49: ",zufallszahl)

# uniform
zufallszahl = random.uniform(1,49)
print("Uniform Zufallszahl 1-49: ",zufallszahl)


# Aufgabe
mein_zufall = random.uniform
zufallszahl = random.uniform(1,5)

# Welche Variable, mein oder der andere erzeugt groessere Zufallszahlen?

print("random.uniform ",mein_zufall) # Ist nur eine Methode dass gebunden wird bound
print(" random.uniform(1,5) ",zufallszahl) #Aus der methode herausgegebene Zufallszahl uniform

#Seite 260 Import from und import as

from random import uniform, randint #Methoden uniform und randint aus dem Modul random importieren
zufallszahl = uniform(1,49)
print(randint(1,49))
print(zufallszahl)

from random import uniform as rand_komma, randint
zufallszahl = rand_komma(1,49)
print(randint(1,49))
print(zufallszahl)

# Nicht gerne gesehen import random *


# Gleich Basis zur Erzeugung der Randomwerte nutzen, ansonsten wird Systemzeit als Basis genutzt

import  random
random.seed(42)

#Aufgabe
import random
from random import random as nullBisEins, randint as zufall

#random.seed(42)
print("zufall(1,10) ",zufall(1,10))
print("nullBisEins() ",nullBisEins())
print("random.randint(1,10) ",random.randint(1,10))

print("random.random() ",random.random())

# Zusammenfassung
"""
Module: Pythonporgramme
Wiederverwendbar
Importierbar

Eigener Namespace

Mit Docstrings kannst Du Doku erstellen, dass mit help() aufgerufen werden kann
Globale Variablen
Mit as auch anderen namen vergeben
"""