"""
Pseudocode: mise à jour
DEBUT
    DEMANDER nom_logiciel
    REPETER
        DEMANDER v_actuelle
        SI v_actuelle INT ET > 0
            ACCEPTER
        SINON
            AFFICHER erreur
    FIN REPETER
    REPETER
        DEMANDER v_nouvelle
        SI v_nouvelle INT ET > v_actuelle
            ACCEPTER
        SINON
            AFFICHER erreur
    FIN REPETER
    AFFICHER "Mises à jour"
    REPETER
        AFFICHER nom_logicier v_actuelle -> nom_logicier v_actuelle+1
        v_actuelle = v_actuelle+1
        SI v_actuelle = v_nouvelle
            TERMINER
    FIN REPETER
FIN
"""
nom_logiciel = input("Quel logiciel voulez-vous mettre à jour? ")
while True:
    try:
        v_actuelle = int(input("Quelle est la version actuelle? "))
        if v_actuelle > 0:
            break
        else:
            print("Erreur : Entrez un nombre positif.")
    except:
        print("Erreur : Entrez un nombre entier.")

while True:
    try:
        v_nouvelle = int(input("Quelle version voulez-vous installer? "))
        if v_nouvelle > v_actuelle:
            break
        else:
            print("Erreur : Entrez une version plus récente.")
    except:
        print("Erreur : Entrez un nombre entier.")

print("\nMises à jour : ")  # \n : saut de ligne
while True:
    print(f"{nom_logiciel} {v_actuelle} -> {nom_logiciel} {v_actuelle+1}")
    v_actuelle = v_actuelle + 1
    if v_actuelle == v_nouvelle:
        break


