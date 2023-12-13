# Klassen - Bauplan Schablone - Spam
# Objekte - eggs = Spam272() Nach Bauplan etwas konkretes - Im Gegensatz zur Funktionen, koennen viel speichern
# Methoden - Die Funktion
# __init__ - Besondere Methode
# Attribute - Eine Variable, der zum Objekt gehört


class Spam272: #CamelCase
    """Eine Spam272 Klasse, nur als einfaches Beispiel"""
    def __init__(self):  # Besondere Methode, einmalig, wenn ein neues Objekt aus einer Klasse erstellt
        print("!INIT: Willkommen in der Klasse Spam!")
        self.ein_attribut = 42 # Ein Attribut!
        # Initialisierung von Attributen
        # Eingabe wichtiger parameter
        # Filestruktur
        # Datenbankbindung
    pass

    """Eine wirklich ganz einfache Klasse. Sie hat keine Fähigkeiten, keine Merkmale
    und auch keine Attribute. Und von einem zugehörigen Objekt ist hier erst mal noch nichts zu sehen"""

    # Methode
    def eine_methode(self):
        print(self.ein_attribut) # Mit dieser Methode, zugriff auf ein Attribut
        #self ist ein besonderer Parameter, den jede Methode einer Klasse benoetigt
        # Uebergabe der internen Infor mit dem self (ist eine Konvention)

        #Instanzieren: Aus der Klasse ein Objekt erschaffen


# Instanzieren: Weise einer Variable eine Klasse zu, und somit wird ein neues Objekt eggs entstehen
eggs = Spam272()
# Zugriff von aussen. Objekt: eggs, Element: eine_methode, Methode: Mit runden Klammern
eggs.eine_methode()
print(eggs.ein_attribut) # Zugriff auf Attribut von aussen


#Zugriff innerhalb einer Klasse
# self.attribut
# self.eine_methode()

# Zugriff ausserhalb einer Klasse
# Klasse.attribut
# Klasse.eine_methode()

# oder Instanziertes Objekt
# objekt = Klasse()
# objekt.attribut
# objekt.eine_methode()
# Jedes Objekt, dass du erschaffst/instanzierst, besitzt alle Attribute, Werte und Methoden der Klassep272_Konstruktor.py