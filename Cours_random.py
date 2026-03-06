import random

for i in range(20):
    nb_entier = random.randint(10, 20) # entier aléatoire entre [10, 20]
    print(nb_entier, end=" ")
print() # saut de ligne
for i in range(20):
    nb_decimal = random.random() # nombre décimal aléatoire entre 0 et 1
    print(nb_decimal)
print()
for i in range(20):
    nb_decimal = random.random() * 10 # nombre décimal aléatoire entre 0 et 10
    print(nb_decimal)
print()
for i in range(20):
    # random décimal dans un intervalle :
    # multiplier par la taille de l'intervalle
    # additionner le minimum de l'intervalle
    nb_decimal = random.random() * 10 + 10 #  entre 10 et 20
    print(nb_decimal)
print()
choix = random.choice(('a', 'b', 'c')) # choix alétoire parmi la liste
print(choix)
print()
for i in range(20):
    distribution = random.uniform(10.0, 20.0)
    print(distribution)
print()

# Valider les entrées utilisateur
while True:
    reponse = input("Est-ce qu'il fait soleil? (o/n) ")
    if reponse == "o" or reponse == "n":
        break # terminer la boucle en cas de réponse valide
    else:
        print("Erreur : Veuillez répondre par o ou n")
print("Vous avez répondu : ", reponse)
while True:
    print("a) Chips")
    print("b) Chocolat")
    print("c) Sucettes")
    choix = input("Quel bonbon tu veux? ")
    if choix == "a":
        print("Crunch crunch")
        break
    elif choix == "b":
        print("Miam")
        break
    elif choix == "c":
        print("Bon choix")
        break
    else:
        print("Choix invalide")
while True:
    age = int(input("Quel âge as-tu? "))
    if age < 0 or age > 120:
        print("Erreur: l'âge doit être entre 0 et 120")
    else:
        break
print("Tu as", age, "ans")