i = 0
while i <= 10:
    print(i, end=" ")
    i += 1 # i = i + 1
print()
a = 10
while a >= 0:
    print(a, end=" ")
    a = a - 1 # a -= 1
print()
b = 10
while b <= 100:
    print(b, end=", ")
    b += 10
print()
somme = 0
while True: # tant que je dis pas d'arrêter, continue!
    nb = int(input("Entre un nombre "))
    if nb == -1: # Vérifier si on a terminé
        break # arrêter la boucle
    somme += nb
print("Somme", somme)