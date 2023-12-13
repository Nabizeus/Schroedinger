# Funktion Orakel von Delphi
import random


class Orakel:

    """Das Orakel gibt dir Antworten auf deine Fragen"""


    def __init__(self,frage):

        self.alte_antwort = None
        self.frage = frage
        self.list_antworten = 'Ja', 'Nein', 'Vielleicht'




    def antwort(self):
        # Mein gescheiterter Versuch




        rand_antwort = random.choice(self.list_antworten)
        return f"Die Antwort auf deine Frage | {self.frage} | lautet: {rand_antwort}"
        #while True:
            #auswahl = random.choice(self.list_antworten)
            #if auswahl != self.alte_antwort:
                #self.alte_antwort = auswahl
                #return auswahl

    #Eine neue Methode ausgabe(), der auf antwort() zugreift
    def ausgabe(this):
        text = f"{this.antwort()}"
        print('#'*len(text))
        print(text)
        print('#' * len(text))






Orakel = Orakel('Sollte ich heiraten?')

for i in range(10):
    print(Orakel.antwort(), end=" \n ")

# Eine neute Methode ausgabe, der auf antwort zugreift

for i in range(5):
    print(Orakel.ausgabe(), end=" \n ")
