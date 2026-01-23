# 2 Convertir des vitesses de transfert (Mbps → MB/s)
# Entrées : vitesses en Mbps
vitesse_connexion_1 = 100
vitesse_connexion_2 = 500
vitesse_connexion_3 = 1000
# Traitement : Conversion de Mbps à MB/s
vitesse_convertie_1 = vitesse_connexion_1/8
vitesse_convertie_2 = vitesse_connexion_2/8
vitesse_convertie_3 = vitesse_connexion_3/8
# Sorties : vitesses en MB/s
print("Vitesse 1:", vitesse_convertie_1, "MB/s")
print("Vitesse 2:", vitesse_convertie_2, "MB/s")
print("Vitesse 3:", vitesse_convertie_3, "MB/s")
print("Vitesses converties:", vitesse_convertie_1, vitesse_convertie_2, vitesse_convertie_3)