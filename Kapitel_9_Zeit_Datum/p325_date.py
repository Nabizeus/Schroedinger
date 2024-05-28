from datetime import date

print(date.today())

# Danke String from time

print(date.today().strftime('%%%d.%m.%Y%')) # Durch Verkettung chaining
print(date.today().strftime("%b ist die Kurzform von %B"))

def ausgabe_zeitreise(datumsObjekt):

    textMuster = "Der %d.%m.%Y war der %-j.Tag des Jahres "

    ergebnis = datumsObjekt.strftime(textMuster)

    return ergebnis


text = ausgabe_zeitreise(date.today())

print(text)

import locale
#locale.setlocale(locale.LC_ALL,'de_DE') Lokalen Wochentagangabenp322_date.py