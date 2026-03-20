"""
somme = 0
POUR 6 FOIS:
    de = RANDOM
    AFFICHER de
    somme += de
moyenne = somme/6
AFFICHER somme
AFFICHER moyenne
"""
import random

somme = 0
for i in range(6):
    type_de = random.randint(6, 20)
    de = random.randint(1, type_de)
    print("Nb de faces", type_de, "\tDé", i+1, ":", de)
    somme += de
moyenne = somme/6
print("Somme: ", somme)
print(f"Moyenne: {moyenne:.1f}")