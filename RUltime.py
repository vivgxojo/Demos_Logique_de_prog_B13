def analyser_chemin(chemin):
    """

    :param chemin:
    :return:
    """
    drive = chemin[0]
    reste = chemin[3:]
    #séparer les parties
    parties = reste.split("\\")
    nb_dossiers = len(parties) - 1
    fichier_complet = parties[-1]
    ls_fichier_complet = fichier_complet.split(".")
    extension = ls_fichier_complet[-1]
    #nom = ""
    #for i in range(len(ls_fichier_complet)-2):
        #nom += ls_fichier_complet[i]
        #nom += "."
    #nom += ls_fichier_complet[-2]
    nom = ".".join(ls_fichier_complet[:-1])
    return drive, nb_dossiers, nom, extension

print(analyser_chemin("F:\\r.1\\r.2\\r.3\\f.1.5.exe"))