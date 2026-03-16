#Exercice 2 : Convertir des vitesses de transfert (Mbps → MB/s)
ls_vitesse = [100, 500, 1000]
ls_vitesse_converties = []

for i in range(len(ls_vitesse)):
    vitesse_mbs = ls_vitesse[i] / 8
    ls_vitesse_converties.append(vitesse_mbs)

for i in range(len(ls_vitesse_converties)):
    print(ls_vitesse[i], "Mbps =", ls_vitesse_converties[i], "MB/s")
print()
#Exercice 4 : Vérifer les ports
ls_ports = [80, 65535, 70000, -5, 22]
for port in ls_ports:
    if port >= 0 and port <= 65535:
        print("Port", port, "valide")
    else:
        print("Port", port, "non valide")

#S1.2, Ex2 : Convertir des tailles de fichiers
ls_fichiers_bytes = [2048, 5242880, 1073741824]
# Constantes de conversion
BYTES_PAR_KB = 1024
BYTES_PAR_MB = 1024 * 1024  # 1048576
BYTES_PAR_GB = 1024 * 1024 * 1024  # 1073741824
for i in range(len(ls_fichiers_bytes)):
    fichier1_kb = ls_fichiers_bytes[i] / BYTES_PAR_KB
    fichier1_mb = ls_fichiers_bytes[i] / BYTES_PAR_MB
    fichier1_gb = ls_fichiers_bytes[i] / BYTES_PAR_GB

    print(f"--- Fichier {i +1 } ---")
    print("Taille:", ls_fichiers_bytes[i], "bytes")
    print("Taille:", fichier1_kb, "KB")
    print("Taille:", fichier1_mb, "MB")
    print("Taille:", fichier1_gb, "GB")