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
        print(f"DAS ORAKEL VON DELPHI PROPHEZEIHT......DINGSBUMS SAMSALABIM ABRA CADABRA")
        print(50*
        "*")

    def stem_leaf(self,list_antw):


        # Given sequence
        sequence = list_antw

        # Interpret the sequence
        interpretation = {
            'J': 'Ja, sie liebt dich noch, und gibt dir ein Bonus-Chance, auch wenn sie nicht will!',
            'N': 'Nein, ihr kommt nicht zusammen! Wtf? Go live your life!',
            'V': 'Vielleicht, aber vlt. auch nicht. Alea iacta est!'
        }

        # Replace letters with interpretations
        interpreted_sequence = [interpretation[letter] for letter in sequence]

        # Count occurrences
        answer_counts = Counter(interpreted_sequence)

        # Create stem-and-leaf display
        stem_and_leaf = {}
        for answer, count in answer_counts.items():
            stem = str(count)
            leaf = answer  # Take the first letter of the interpreted answer
            if stem not in stem_and_leaf:
                stem_and_leaf[stem] = []
            stem_and_leaf[stem].append(leaf)

        # Display the results
        sorted_leaf = sorted(stem_and_leaf.items(), key=lambda x: int(x[0]))
        print(self.ausgabe(),sorted_leaf[-1][1][0])

        for stem, leaves in sorted_leaf:

            print(f'{stem} | {" ".join(sorted(leaves))}')


# Instanzieren: Weise einer Variable eine Klasse zu, und somit wird ein neues Objekt eggs entstehen
orakel = Orakel()
list_antw = []
# Zugriff von aussen. Objekt: eggs, Element: eine_methode, Methode: Mit runden Klammern
for i in range(10000):
    list_antw.append(orakel.weissagt())



orakel.stem_leaf(list_antw)