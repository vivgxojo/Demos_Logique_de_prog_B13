# Exercice 5 : Calculer le nombre d'hôtes disponibles dans un sous-réseau
def calculer_hotes_disponibles(cidr):
    """
    Calculer le nombre d'hôtes disponibles dans un sous-réseau
    :param cidr: CIDR du sous-réseau
    :return: le nombre d'hôtes disponibles
    """
    nb_hotes = 2 ** (32 - cidr) - 2 # Calculs (formule: 2^(32-CIDR) - 2)
    return nb_hotes

# Données
ls_cidr = [24, 25, 26, 30]
ls_nb_hotes = []

for cidr in ls_cidr:
    nb_hotes = calculer_hotes_disponibles(cidr)
    ls_nb_hotes.append(nb_hotes)

# Affichage
for i in range(len(ls_cidr)):
    print("Sous-réseau /" + str(ls_cidr[i]), ":", ls_nb_hotes[i], "hôtes disponibles")

# Résultats attendus:
# Sous-réseau /24: 254 hôtes disponibles
# Sous-réseau /25: 126 hôtes disponibles
# Sous-réseau /26: 62 hôtes disponibles
# Sous-réseau /30: 2 hôtes disponibles