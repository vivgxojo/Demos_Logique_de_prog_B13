def analyser_port(port):
    """
    Déterminer la catégorie d'un port
    :param port: port à analyser
    :return: catégorie du port
    """
    # Vérifier la validité du port et déterminer la catégorie
    try:
        if port < 0:
            categorie = "Erreur : Le numéro de port ne peut pas être négatif."
        elif port > 65535:
            categorie = "Erreur : Le numéro de port ne peut pas dépasser 65535."
        elif port <= 1023:
            categorie = "Ports bien connus"
        elif port <= 49151:
            categorie = "Ports enregistrés"
        else:
            categorie = "Ports dynamiques/privés"
        return categorie
    except:
        return "Erreur : le port doit être numérique"
