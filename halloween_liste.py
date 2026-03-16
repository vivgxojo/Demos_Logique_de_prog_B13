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
for maison in ls_maison:
    reponse = input("Donne des bonbons? ")
    if reponse == "oui":
        bonbons = int(input("Combien de bonbons? "))
        ls_bonbons.append(bonbons)
somme = 0
for i in range(len(ls_bonbons)):
    somme += ls_bonbons[i]
moyenne = somme/len(ls_maison)
print("Total : ", somme)
print("Moyenne : ", moyenne)