"""
ls_bonbons = []
ls_maison = [les adresses]
POUR CHAQUE MAISON
    DEMANDER si elle donne des bonbons
    SI oui:
        DEMANDER des bonbons
        AJOUTER bonbons à la liste
COMPTER les bonbons
COMPTER la moyenne
"""
ls_bonbons = []
ls_maison = [10, 12, 14, 16, 18, 20]
ls_genereux = []
for maison in ls_maison:
    reponse = input(f"Adresse {maison} : donne des bonbons? ")
    if reponse == "oui":
        bonbons = int(input("Combien de bonbons? "))
        ls_bonbons.append(bonbons)
        ls_genereux.append(maison)
somme = sum(ls_bonbons)
moyenne = somme/len(ls_genereux)
print("Total de bonbons : ", somme)
print("Moyenne de bonbons par maison généreuse : ", moyenne)
print("Nombre de maisons fermées : ", len(ls_maison) - len(ls_genereux))
max_bonbons = max(ls_bonbons)
print("Max de bonbons donnés par une maison : ", max_bonbons)
indice_plus_genereux = ls_bonbons.index(max_bonbons)
print("Adresse de la maison la plus généreuse : ", ls_genereux[indice_plus_genereux])