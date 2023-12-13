
import pickletools # Kann importiert werden ohne as
pckl = pickletools # als Variable zuwesen
select = pckl.int4(a,b,c)
select_new = pickletools.int4(a,b,c) # Beide Varianten moeglich

# Syntaktisches Zucker
