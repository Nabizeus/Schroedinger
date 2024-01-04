# Getter and Setter

""" Getter und Setter sind keine Sache der Syntax oder der jeweiligen Programmiersprache
Sie sind eine Konvention:
    Soll ein Attribut verandert werde, so wird das uber eine spezielle Methode gemacht
    Die Methode nimmt ein Wert entgegen, uberpruft und passt an
    Erst wenn alles in OPrdnung ist, wird der neue Wert in das Attribut geschrieben
    Diese Methode ist der Setter
    Der tatsächliche Name so einer Methode setzt sich meist aus set und dem Namen des Attributs
    set_temperatur für Temperatur

    Auslesen über GetterÖ
    Damit intern etwas prozessiert wird, zb Fahrenheit in Celsicus umwandeldn, das wäre durch Getter
    get_tempeeratur."""

class Spam: # Nie negative Zahlen zulassen
    def __init__(self): # Hier initialisieren wir das Attribut, um das es geht. Die eigenartige ist privat. Kein Zugriff
        self.__nummer = 0
    def set_nummer(self, wert): #Klassischer Setter. Dies verwenden um die nummer zu aendern
        self.__nummer = abs(wert) # Wird geprueft. Mit Absolut wird jeder positiv.
    def get_nummer(self): # Klassicher Getter. Den Wert gibt es zurück, auch modifiziert, zb als int
        return int(self.__nummer) # Attribut ist float und soll so sein. Jedoch der Wert als Interger ausgeben

    nummer = property(get_nummer,set_nummer)
egg = Spam()
egg.set_nummer(-15.5) # __nummer wird im Objekt yu 15.5. Setter muss explizit aufgerufen werden.
print(egg.get_nummer())  #Durch getter koennen wir Zugriff auf Private variable __nummer zugreifen. Intern kein Aendrung.


# Das ist aber kein Pythonway

# Dafuer Property Funktion!

egg.nummer = -17.6
print(egg.nummer)

