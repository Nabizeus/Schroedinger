from datetime import date

print(date.today())

# Danke String from time

print(date.today().strftime('%d.%m.%Y')) # Durch Verkettung chaining
print(date.today().strftime("Wir schreiben das Jahr %Y"))

def ausgabe_zeitreise(datumsObjekt):
    textMuster = "Im %m.Monat des Jahres %Y verschwand "\
    "der Zeitreisende Schroedinger."
    ergebnis = datumsObjekt.strftime(textMuster)

    return ergebnis


text = ausgabe_zeitreise(date.today())

print(text)

import locale
#locale.setlocale(locale.LC_ALL,'de_DE') Lokalen Wochentagangabenp322_date.py