for i in range(0, 11, 1): # [1, 11[, saut
    print(i, end=", ") # sur la même ligne
print() # saut de ligne
for i in range(5, 31, 5):
    print(i, end=", ")
print()
for i in range(100, 0, -10):
    print(i, end=", ")
print()
for i in range(10): #[0, 10[, saut=1
    print(i, end=", ")
print()
for i in range(10, 20): #[10, 20[, saut=1
    print(i, end=", ")
print()
# Additionner des nombres entrés par l'utilisateur
somme = 0
for i in range(5): # répéter 5 fois
    nb = int(input("Entre un nombre "))
    somme = somme + nb
print("Somme:", somme)
print()
# Transformer toutes les notes en pourcentage
# Calculer la moyenne
somme_notes = 0
nb_notes_valides = 0
for i in range(10):
    note = int(input("Entre une note sur 50 "))
    if note < 0 or note > 50:
        print("Note invalide")
    else:
        nb_notes_valides += 1
        pourcentage = note * 100 / 50
        somme_notes += pourcentage # somme_note = somme_note + pourcentage
        print(f"{pourcentage:.0f}%")
moyenne = somme_notes/nb_notes_valides
print(f"{moyenne:.0f}%")