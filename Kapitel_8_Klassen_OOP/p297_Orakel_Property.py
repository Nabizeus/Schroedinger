import random
from collections import Counter

class Orakel: #CamelCase
    """Das Orakel von Delphi mit Ja, Nein, Vielleicht als Antwort, keine Wiederholung"""
    def __init__(self):  # Besondere Methode, einmalig, wenn ein neues Objekt aus einer Klasse erstellt
        """Initialisierung der Antworten...."""

        print("Willkommen bei der Orakel von DELPHI! Gib deine Frage...Gibt es eine Chance bei Elena???")
        self.letzte_antwort = None
        self.antwort_liste = ("J","N","V") # Ein Attribut!

    # Methode
    def weissagt(self):
        # Nur eine Variable

        while True:# Solange die Schleife laufen lassen bis eine IF Anweisung falsch laueft

            antwort = random.choice(self.antwort_liste) # Mit dieser Methode,Zugriff auf ein Klasseninternes Attribut


            if antwort != self.letzte_antwort: # Erst wenn die Auswahl ungleich ist, dann wird die Schleife verlassen

                self.letzte_antwort = antwort

                return antwort

    def ausgabe(self):

        print(50*"*")
        print(f"DAS ORAKEL VON DELPHI PROPHEZEIHT......DINGSBUMS SAMSALABIM ABRA CADABRA... {self.weissagt()}")
        print(50*
        "*")




# Instanzieren: Weise einer Variable eine Klasse zu, und somit wird ein neues Objekt eggs entstehen
orakel = Orakel()
list_antw = []
# Zugriff von aussen. Objekt: eggs, Element: eine_methode, Methode: Mit runden Klammern
for i in range(10000):
    list_antw.append(orakel.weissagt())
print("list_antw[-3:-1]",list_antw[-10:-1])
orakel.ausgabe()
# Zugriff auf Attribut self.antwort_liste @__init__ und diese wieder veraendern
orakel.antwort_liste = ("Geh nach Barcelona!!!","Geh NICHT nach Barcelona!","Frag Elena, Cava, Goettingen?")
orakel.ausgabe()

orakel.antwort_liste = "Tus nicht, Schr0edinger!"

for i in range(9):
    print(orakel.weissagt(), end=" ")
