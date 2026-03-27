liste = []
while True:
    print("Ajouter serveur DNS")
    print("Afficher liste de serveurs DNS")
    print("Supprimer serveur DNS")
    choix = input("Que voulez-vous faire? (ajouter/afficher/supprimer) ")
    if choix == "ajouter":
        while True:
            dns = input("Entrez l'adresse du serveur DNS : (ex 10.10.10.10) ")
            if dns == "fin":
                break
            liste.append(dns)
    elif choix == "afficher":
        print(liste)
    elif choix == "supprimer":
        dns_a_supp = input("Quelle est l'adresse du serveur DNS à supprimer? ")
        if dns_a_supp in liste: # vérifier si l'item existe dans la liste
            liste.remove(dns_a_supp)
        else:
            print("Erreur : Serveur innexistant")
