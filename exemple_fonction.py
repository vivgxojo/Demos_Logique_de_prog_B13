def convertir_vitesse(vitesse_mbps):
    """
    Convertir des vitesses de transfert (Mbps → MB/s)
    :param vitesse_mbps: vitesse en Mbps
    :return: vitesse en MB/s
    """
    vitesse_mbs = vitesse_mbps / 8
    return vitesse_mbs

# Données
ls_vitesses_mbps = [100, 500, 1000]
ls_vitesses_mbs = [] # liste pour mettre les vitesses converties
for vitesse in ls_vitesses_mbps:
    ls_vitesses_mbs.append(convertir_vitesse(vitesse))

for i in range(len(ls_vitesses_mbs)):
    print(ls_vitesses_mbps[i], "Mbps =", ls_vitesses_mbs[i], "MB/s")