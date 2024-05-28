
class MachWas:
    """Klassen Methode?"""

    counter = 0 # Klassenattribut
    #MachWas.counter = 1 # T#his does not work

    def aufruf(self):

        print("Ich tue mal was")
        MachWas.counter +=1

    # STATIC METHOD; Methoden, die ohne Objekt verwendet werden koennen

    # def aufruf(self): Nur durch Objekt aufrunfbar, daher self notwending
    # @staticmethod
    # def ausgabe(wert): Ohne Objekt aufrubar, daher kein self notwending
    @staticmethod #Dekorator
    def upper(wert):
        print(wert.upper())


print(MachWas)
print(MachWas.counter)
print(MachWas.counter)
print(MachWas().aufruf())
obj = MachWas()
print(obj.aufruf())
print(MachWas.counter)
print(MachWas.counter)
obj.aufruf()
print(MachWas.counter)

MachWas.upper("Hallo Schroedinger")