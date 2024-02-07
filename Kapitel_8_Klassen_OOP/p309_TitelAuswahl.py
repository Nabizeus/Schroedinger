from p307_EinmaligeAntwort import EinmaligeAntwort
class TitelAuswahl(EinmaligeAntwort):
    """Vererbte Funktion p307"""

    def __init__(self,eingabe):  # Besondere Methode, einmalig, wenn ein neues Objekt aus einer Klasse erstellt
        """Initialisierung der Antworten...."""

        print("Willkommen bei der TitelAuswahl")
        self.alte_antwort = None
        self.antwort_liste = tuple(range(eingabe))







song = TitelAuswahl(99)


for i in range(10):
    print(song.select(), end=" ")