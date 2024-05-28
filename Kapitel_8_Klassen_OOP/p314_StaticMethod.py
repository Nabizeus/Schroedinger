from p307_EinmaligeAntwort import EinmaligeAntwort
class TitelAuswahl(EinmaligeAntwort): #Titelauswahl diese Klasse bzw. abgeleit Klasse. EinmaligeAntwort Urklasse
    """Vererbte Funktion p307"""

    def __init__(self,eingabe):  # Besondere Methode, einmalig, wenn ein neues Objekt aus einer Klasse erstellt
        """Initialisierung der Antworten...."""

        print("Willkommen bei der TitelAuswahl")
        self.alte_antwort = None
        self.antwort_liste = tuple(range(eingabe))

        super(TitelAuswahl, self).__init__(12) # Mit super der Init von Urklasse aufgeruffen







song = TitelAuswahl(99)


for i in range(10):
    print(song.select(), end=" ")