# Exercice 2 : Convertir des vitesses de transfert (Mbps → MB/s)
# Données
vitesse_mbps_1 = 100
vitesse_mbps_2 = 500
vitesse_mbps_3 = 1000

# Conversion (diviser par 8 car 1 octet = 8 bits)
vitesse_mbs_1 = vitesse_mbps_1 / 8
vitesse_mbs_2 = vitesse_mbps_2 / 8
vitesse_mbs_3 = vitesse_mbps_3 / 8

# Affichage
print(vitesse_mbps_1, "Mbps =", vitesse_mbs_1, "MB/s")
print(vitesse_mbps_2, "Mbps =", vitesse_mbs_2, "MB/s")
print(vitesse_mbps_3, "Mbps =", vitesse_mbs_3, "MB/s")
print()

# Résultats attendus:
# 100 Mbps = 12.5 MB/s
# 500 Mbps = 62.5 MB/s
# 1000 Mbps = 125.0 MB/s

# Version S6
# Convertir 5 vitesses au choix de l’utilisateur
for i in range(5):
    vitesse = float(input("Entrez une vitesse en Mbps: "))
    vitesse_convertie = vitesse / 8
    print(f"{vitesse_convertie} MB/s")