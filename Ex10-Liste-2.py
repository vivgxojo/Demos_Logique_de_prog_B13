"""
liste = []
RÉPÉTER
    DEMANDER ip
    SI ip == "fin"
        BREAK
    SINON
        AJOUTER ip DANS liste
AFFICHER longueur de la liste
ESSAYER
    AFFICHER liste[0]
    AFFICHER liste[-1]
    AFFICHER liste[longueur//2]
ATTRAPPER erreur
    AFFICHER erreur
"""

liste = []
while True:
    ip = input("Entrez l'adresse IP à ajouter ou fin pour terminer ")
    if ip == "fin":
        break
    else:
        liste.append(ip)
print("Nombre d'adresse IP:", len(liste))
try:
    print("Première:", liste[0])
    print("Dernière:", liste[-1])
    print("Milieu:", liste[len(liste)//2])
except IndexError: 
    print("La liste est vide")
