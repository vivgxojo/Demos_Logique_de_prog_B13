"""
FONCTION analyser_ressource (ls_cpu, ls_ram)
    moyenne_cpu = sum(ls_cpu)/len(ls_cpu)
    moyenne_ram = sum(ls_ram)/len(ls_ram)
    alertes = []
    POUR i de 0 à len(ls_cpu)
        SI ls_cpu[i] > 90 ET ls_ram[i] > 90:
            AJOUTER alerte critique
        SINON SI ls_cpu[i] > 90:
            AJOUTER alerte cpu
        SINON SI ls_ram[i] > 90:
            AJOUTER alert ram
    RETOURNER moyenne_cpu, moyenne_ram, alertes
"""
def analyser_ressource (ls_cpu, ls_ram):
    if len(ls_cpu) == 0 or len(ls_ram) == 0:
        # obligé de retourner toujours le même nombre de variables
        return -1, -1, ["Erreur : liste vide"]
    elif len(ls_cpu) > 24 or len(ls_ram) > 24:
        return -1, -1, ["Erreur : liste trop longue"]
    elif len(ls_cpu) != len(ls_ram):
        return -1, -1, ["Erreur : les listes n'ont pas la même longueur"]
    try:
        moyenne_cpu = sum(ls_cpu)/len(ls_cpu)
        moyenne_ram = sum(ls_ram)/len(ls_ram)
    except:
        return -1, -1, ["Erreur : les valeurs doivent être des nombres"]
    alertes = []
    for i in range(len(ls_cpu)):
        if ls_cpu[i] > 100 or ls_cpu[i] < 0 or ls_ram[i] > 100 or ls_ram[i] < 0:
            return -1, -1, ["Erreur : les valeurs doivent être entre 0 et 100 %"]
        if ls_cpu[i] > 90 and ls_ram[i] > 90:
            alertes.append("Alerte critique : cpu (" + str(ls_cpu[i]) + "%) et ram (" + str(ls_ram[i]) + "%) dépassent 90% à " + str(i) + "h.")
        elif ls_cpu[i] > 90:
            alertes.append(f"Alerte intermédiaire : cpu utilisé à {ls_cpu[i]}% à {i}h.")
        elif ls_ram[i] > 90:
            alertes.append(f"Alerte intermédiaire : ram utilisé à {ls_ram[i]}% à {i}h.")
    return moyenne_cpu, moyenne_ram, alertes

