# Les listes
# indice :    0, 1, 2, 3,   4, 5, 6
ls_nombres = [1, 3, 8, 40, 9, 10, 50]
ls_mots = ["allo", "bonjour", "salut", "hello"]
ls_prix = [2.44, 5.66, 10.91, 9.99, 75.50, 56.00, 12.20]
print(ls_mots[2]) # accéder à un item par son indice
ls_nombres.append(60) # ajouter à la fin de la liste
ls_mots.insert(2, "yo") # insérer où on veut dans la liste
ls_nombres.insert(0, 100)
del ls_prix[0]  #supprimer un item de la liste
print(ls_mots[1:3]) # indices [1, 3[
print(ls_nombres[:5]) # indices [0, 5[
print(ls_prix[3:]) # indices 3 à la fin
print(ls_nombres[1:len(ls_nombres):2]) # indices 1 au dernier, bonds de 2
print("Nb de nombres", len(ls_nombres))
print("Nb de mots", len(ls_mots))
print("Nb de prix", len(ls_prix))
print(ls_mots[len(ls_mots)-1]) # trouve le dernier item
ls_mots.remove("hello") # supprimer un item
ls_nombres[1] = 500 # modifier un item
print(ls_nombres)
print(ls_mots)
print(ls_prix)
for i in range(len(ls_nombres)): # i correspond à chaque indice de la liste
    print(f"Indice {i}, item {ls_nombres[i]}")
for mot in ls_mots: # mot correspond à chaque item de la liste
    print(mot)
print("Les prix sont :", end=" ")
for j in range(len(ls_prix)):
    print(f"{ls_prix[j]:.2f}", end="$ ")
print()
position = ls_mots.index("salut") # trouver l'indice d'un item
print(position)