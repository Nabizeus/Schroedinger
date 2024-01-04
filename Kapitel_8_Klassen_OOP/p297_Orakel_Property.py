import random
from collections import Counter

class Orakel: #CamelCase
    """Das Orakel von Delphi mit Ja, Nein, Vielleicht als Antwort, keine Wiederholung"""
    def __init__(self):  # Besondere Methode, einmalig, wenn ein neues Objekt aus einer Klasse erstellt
        """Initialisierung der Antworten...."""

        print("Willkommen bei der Orakel von DELPHI! Gib deine Frage...Gibt es eine Chance bei Elena???")
        self.letzte_antwort = None
        self.__antwort_liste = ("J","N","V") # Ein Attribut!

    # Methode
    def weissagt(self):
        # Nur eine Variable

        while True:# Solange die Schleife laufen lassen bis eine IF Anweisung falsch laueft

            antwort = random.choice(self.__antwort_liste) # Mit dieser Methode,Zugriff auf ein Klasseninternes Attribut


            if antwort != self.letzte_antwort: # Erst wenn die Auswahl ungleich ist, dann wird die Schleife verlassen

                self.letzte_antwort = antwort

                return antwort

    def ausgabe(self):

        print(50*"*")
        print(f"DAS ORAKEL VON DELPHI PROPHEZEIHT......DINGSBUMS SAMSALABIM ABRA CADABRA... {self.weissagt()}")
        print(50*
        "*")

    def lies_antworten(self): #Klassischer Setter. Dies verwenden um die nummer zu aendern
        return self.__antwort_liste
    def neue_antworten(self,neue_antworten): # Klassicher Getter. Den Wert gibt es zurück, auch modifiziert, zb als int
        if isinstance(neue_antworten, (tuple, list)):
            self.__antwort_liste = neue_antworten

    antworten = property(lies_antworten, neue_antworten)


# Instanzieren: Weise einer Variable eine Klasse zu, und somit wird ein neues Objekt eggs entstehen
orakel = Orakel()
list_antw = ("ASD","dadlkjf","£$£$")

print(orakel.weissagt())

orakel.antworten = list_antw

print(orakel.weissagt())
