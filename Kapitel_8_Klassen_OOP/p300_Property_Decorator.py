# Getter and Setter

""" @ Property"""

class Spam: # Nie negative Zahlen zulassen
    def __init__(self): # Hier initialisieren wir das Attribut, um das es geht. Die eigenartige ist privat. Kein Zugriff
        self.__nummer = 0
    @property
    def nummer(self):
        """Die Property fuer immer"""

    @nummer.setter
    def nummer(self, wert):
        self.__nummer = abs(wert)
    @nummer.getter
    def nummer(self): # Klassicher Getter. Den Wert gibt es zurück, auch modifiziert, zb als int
        return int(self.__nummer) # Attribut ist float und soll so sein. Jedoch der Wert als Interger ausgeben


egg = Spam()
egg.nummer = -15.5 # __nummer wird im Objekt yu 15.5. Setter muss explizit aufgerufen werden.
print(egg.nummer)  #Durch getter koennen wir Zugriff auf Private variable __nummer zugreifen. Intern kein Aendrung.


# Das ist aber kein Pythonway

# Dafuer Property Funktion!

egg.nummer = -17.6
print(egg.nummer)

