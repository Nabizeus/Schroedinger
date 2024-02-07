import random
from collections import Counter

class EinmaligeAntwort: #CamelCase
    """Das Orakel von Delphi mit Ja, Nein, Vielleicht als Antwort, keine Wiederholung"""
    def __init__(self,eingabe):  # Besondere Methode, einmalig, wenn ein neues Objekt aus einer Klasse erstellt
        """Initialisierung der Antworten...."""

        print("Willkommen bei der Orakel von DELPHI! Gib deine Frage...Gibt es eine Chance bei Elena???")
        self.alte_antwort = None
        if isinstance(eingabe,(tuple,list)):

            self.__antwort_liste = eingabe

    # Methode
    def select(self):
        # Nur eine Variable

        while True:# Solange die Schleife laufen lassen bis eine IF Anweisung falsch laueft

            auswahl = random.choice(self.__antwort_liste) # Mit dieser Methode, Zugriff auf ein Klasseninternes Attribut


            if auswahl != self.alte_antwort: # Erst wenn die Auswahl ungleich ist, dann wird die Schleife verlassen

                self.alte_antwort = auswahl

                return auswahl



# Instanzieren: Weise einer Variable eine Klasse zu, und somit wird ein neues Objekt eggs entstehen

list_antw = ("Ja","Nein","Vielleicht ;)")
antwort = EinmaligeAntwort(list_antw)
print(antwort.select())

antwort.antworten = list_antw

print(antwort.select())
