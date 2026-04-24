def verifier_acces(blacklist, ip):
    """
    Vérifier si une adresse ip a accès
    :param blacklist: liste d'adresses malveillantes
    :param ip: adresse ip à vérifier
    :return: vrai ou faux selon si l'adresse est autorisée ou non
    """
    if ip in blacklist:
        return False
    else:
        return True