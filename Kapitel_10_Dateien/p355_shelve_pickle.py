import shelve

spieler_endrunde = ['Amelia','Elena','Maria']
mein_speicher = shelve.open('meineDaten.db')
mein_speicher['imFinale'] = spieler_endrunde
print(mein_speicher['imFinale'])
spieler = mein_speicher['imFinale']

for name in spieler:
    print(name)
mein_speicher.close()
