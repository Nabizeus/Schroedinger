# Klassen - Bauplan Schablone - Spam
# Objekte - eggs = Eggs() Nach Bauplan etwas konkretes - Im Gegensatz zur Funktionen, koennen viel speichern
# Methoden - Wie Funktion
# __init__ - Besondere Methode
# Attribute - Eine Variable, der zum Objekt gehört, wird immer mit self. vorgesetzt. Ohne self. ist es eine Variable
from p272_Konstruktor import Spam272

class Eggs: #CamelCase
    """Eine Eggs Klasse, nur als einfaches Beispiel"""
    def __init__(self):  # Besondere Methode, einmalig, wenn ein neues Objekt aus einer Klasse erstellt
        print("!INIT: Willkommen in der Klasse Eggs!")
        self.ein_attribut = 42 # Ein Attribut!
        # Initialisierung von Attributen
        # Eingabe wichtiger parameter
        # Filestruktur
        # Datenbankbindung

    """Eine wirklich ganz einfache Klasse. Sie hat keine Fähigkeiten, keine Merkmale
    und auch keine Attribute. Und von einem zugehörigen Objekt ist hier erst mal noch nichts zu sehen"""

    # Methode
    def eine_methode(self):
        # Nur eine Variable
        verdoppelt = self.ein_attribut*2 # Mit dieser Methode,Zugriff auf ein Klasseninternes Attribut
        print("self.ein_attribut ",self.ein_attribut)
        print("verdoppelt ",verdoppelt)


# Instanzieren: Weise einer Variable eine Klasse zu, und somit wird ein neues Objekt eggs entstehen
eggs = Eggs()
# Zugriff von aussen. Objekt: eggs, Element: eine_methode, Methode: Mit runden Klammern
eggs.eine_methode()
print("eggs.ein_attribut",eggs.ein_attribut) # Zugriff auf Attribut von aussen
print("eggs.__doc__",eggs.__doc__)
print("Spam272.__doc__",Spam272.__doc__)
help(eggs)
help(Spam272)