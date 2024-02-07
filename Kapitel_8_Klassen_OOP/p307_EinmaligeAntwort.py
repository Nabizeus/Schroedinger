import random
from collections import Counter

class EinmaligeAntwort: #CamelCase
    """Das Orakel von Delphi mit Ja, Nein, Vielleicht als Antwort, keine Wiederholung"""
    def __init__(self,eingabe):  # Besondere Methode, einmalig, wenn ein neues Objekt aus einer Klasse erstellt
        """Initialisierung der Antworten...."""

        print("Willkommen bei der EinmaligeAntwort ohne Wiederholung")
        self.alte_antwort = None
        if isinstance(eingabe,(tuple,list)):

            self.antwort_liste = eingabe

    # Methode
    def select(self):
        # Nur eine Variable

        while True:# Solange die Schleife laufen lassen bis eine IF Anweisung falsch laueft

            auswahl = random.choice(self.antwort_liste)


            if auswahl != self.alte_antwort: # Erst wenn die Auswahl ungleich ist, dann wird die Schleife verlassen

                self.alte_antwort = auswahl

                return auswahl
