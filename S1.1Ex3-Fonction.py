# Exercice 3 : Calculer le temps de téléchargement d'un fichier
def convertir_fichier(taille_fichier_gb, vitesse_mbps):
    """
    Conversions de fichiers de gb à mb et de la vitesse de mbps à mbs
    :param taille_fichier_gb: taille du fichier en gb
    :param vitesse_mbps: vitesse en mbps
    :return: taille du fichier en mb et vitesse en mbs
    """
    taille_fichier_mb = taille_fichier_gb * 1024  # GB en MB
    vitesse_mbs = vitesse_mbps / 8  # Mbps en MB/s
    return taille_fichier_mb, vitesse_mbs

def calculer_temps_telechargement(taille_fichier_mb, vitesse_mbs):
    """
    Calculer le temps de téléchargement en minutes et en secondes
    :param taille_fichier_mb: taille du fichier en mb
    :param vitesse_mbs: vitesse en mbs
    :return: temps en seconde et temps en minutes
    """
    temps_secondes = taille_fichier_mb / vitesse_mbs
    temps_minutes = temps_secondes / 60
    return temps_secondes, temps_minutes

# Programme principal
# Données
taille_fichier_gb = 4.7  # GB
vitesse_mbps = 50  # Mbps

taille_fichier_mb, vitesse_mbs = convertir_fichier(taille_fichier_gb, vitesse_mbps)
temps_secondes, temps_minutes = calculer_temps_telechargement(taille_fichier_mb, vitesse_mbs)

# Affichage
print("Taille du fichier:", taille_fichier_gb, "GB =", taille_fichier_mb, "MB")
print("Vitesse de téléchargement:", vitesse_mbps, "Mbps =", vitesse_mbs, "MB/s")
print("Temps de téléchargement:", temps_secondes, "secondes")
print("Temps de téléchargement:", temps_minutes, "minutes")
print("Temps de téléchargement:", round(temps_minutes, 2), "minutes")
print()

# Résultats attendus:
# Taille du fichier: 4812.8 MB
# Vitesse: 6.25 MB/s
# Temps: 770.048 secondes ≈ 12.83 minutes