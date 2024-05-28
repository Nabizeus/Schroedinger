import re

## So kann ich ein Block?

text = "Written 2021 annum May monum 24 daium 20 chronum " #May 2021, 24, at 20 o'clock."
suche = "Written .*? chronum" #o'clock."
treffer = re.search(suche,text)

print("target: ",treffer[0])


#Get the target value and convert it into datetime

from datetime import datetime
import locale
#locale.setlocale(locale.LC_ALL,'DE_de')
zeitMuster = "Written %Y annum %B monum %d daium %H chronum" #%B %Y, %d. at %H o'clock."
print("zeitMuster",zeitMuster)
zeitObjekt = datetime.strptime(treffer[0], zeitMuster)
print("zeitObjekt",zeitObjekt)
