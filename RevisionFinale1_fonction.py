def analyser_ping(ls_ping):
    """
    Analyser une liste de 5 pings
    :param ls_ping: les temps des pings
    :return: le temps moyen, le min, le max et un verdict
    """
    moyenne = sum(ls_ping)/len(ls_ping)
    minimum = min(ls_ping)
    maximum = max(ls_ping)
    if moyenne < 80:
        verdict = "Connexion STABLE"
    elif moyenne <= 150:
        verdict = "Connexion INSTABLE"
    else:
        verdict = "Connexion CRITIQUE"
    return moyenne, minimum, maximum, verdict