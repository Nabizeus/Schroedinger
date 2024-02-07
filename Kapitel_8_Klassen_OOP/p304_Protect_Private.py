# Public Private & Proteced

""" @ Property"""

class Spam304:
    def __init__(self):
        self._steuersatz = 7 #1 Hier haben wir einen Wert der Protected ist fuer aussen

    def __berechne(self, preis): #2 Diese Methode ist private. Kann nur innerhalb der Klasse aufgerufen werden
        """Die Property fuer immer"""
        return preis*(1+0.01*self._steuersatz) #3 Das Proteced Attribut _steuersatz fuer Berechnung. Moeglich da intern

    def wert(self, wert): #4 Diese Methode ist Public. Es benutzt die Proteced und Private Methoden
        ergebnis = int(self.__berechne(wert)) #5 Das Private Methode __berechne fuer Ausgabe. Moeglich da intern.
        print(f"Bruttowert fuer den Kauf mit dem {self._steuersatz: .2f} % Steuersatz: {ergebnis: .2f} €")

brutto = Spam304()

brutto.wert(300)

#---------------Falls versuchte wird auf Protected zuzugreifen

brutto._steuersatz = 8 #3 Der Zugriff auf _steuersatz ist Moeglich aber sollte nicht gemacht werden

brutto.wert(300)

#---------------Falls versuchte wird auf Private zuzugreifen
print("brutto.__dir__() ",brutto.__dir__()) #Python bennent die Private Sachen in ein Proteced, also hier __berechne ins _Spam304__berechne um
brutto.__berechne(500)
