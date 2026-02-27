# Entrées
# nb de bonbons de chaque sortes

# Calculs
# Le nombre de maisons total
# Le nombre de maisons qui donnent des bonbons
# Total de bonbons
# Nb de bonbons par maisons en moyenne

total_bonbons = 0
total_maisons = 0
nb_maisons = 0
while True:
    donne = bool(input("Toc-toc-toc")) # appuyer sur Enter pour dire non (False)
    total_maisons += 1
    if donne: # if donne == True:
        nb_bonbons = int(input("Combien de bonbons? "))
        sorte = input("Quelle sorte? ")
        total_bonbons += nb_bonbons
        nb_maisons += 1
        if total_bonbons > 100:
            break
moyenne = total_bonbons/nb_maisons
print("Total de bonbons", total_bonbons)
print("Nb de maison total", total_maisons)
print("Nb de maison qui ont donné des bonbons", nb_maisons)
print("Moyenne", moyenne)