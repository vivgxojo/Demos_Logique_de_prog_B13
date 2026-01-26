# Entrer des données à la console : variable = input("Question ")
texte = input("Entre un mot : ")
print(type(texte))
print(texte)

nombre_entier = int(input("Entre un nombre entier : "))
print(type(nombre_entier))
print(nombre_entier)

nombre_decimal = float(input("Entre un nombre décimal : "))
print(type(nombre_decimal))
#print(f... formater le nombre de décimal
print(f"Le nombre est : {nombre_decimal:.2f}.")
# "texte" + str(variable) : concaténer des variables et du texte
print("Le nombre entier est : " + str(nombre_entier) + ".")
print(f"Mes variables : {texte}, {nombre_entier}, {nombre_decimal:.1f}")
print("-" * 30) # * répéter la chaine à afficher
#f :<20 colonne alignée à gauche, largeur 20, :^5 centrer, :>10 aligner à droite
print(f"{texte:<20} {nombre_entier:^5} {nombre_decimal:>10}")
print(f"{nombre_decimal:<20} {nombre_entier:^5} {texte:>10}")