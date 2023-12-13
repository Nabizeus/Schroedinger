# Klassen - Bauplan Schablone
# Objekte - Nach Bauplan etwas konkretes - Im Gegensatz zur Funktionen, koennen viel speichern
# Methoden
# Attribute


class Spam270: #CamelCase

    pass

    """Eine wirklich ganz einfache Klasse. Sie hat keine Fähigkeiten, keine Merkmale
    und auch keine Attribute. Und von einem zugehörigen Objekt ist hier erst mal noch nichts zu sehen"""

    # Methode
    def eine_methode(self):
        print(42)
        #self ist ein besonderer Parameter, den jede Methode einer Klasse benoetigt
        # Uebergabe der internen Infor mit dem self (ist eine Konvention)

        #Instanzieren: Aus der Klasse ein Objekt erschaffen


# Instanzieren: Weise einer Variable eine Klasse zu, und somit wird ein neues Objekt eggs entstehen
eggs = Spam270()
# Zugriff von aussen. Objekt: eggs, Element: eine_methode, Methode: Mit runden Klammern
eggs.eine_methode()