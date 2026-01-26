# Nouvelle interface réseau
# Entrées
Adresse_IP = input("Entrez l'adresse IP : ")
Masque = int(input("Entrez le masque : /"))

# Traitements
Nb_bits_reseau = Masque
Nb_bits_hotes = 32 - Masque
Nb_adresses = 2 ** Nb_bits_hotes
Nb_hotes_util = 2 ** Nb_bits_hotes - 2

# Sorties
print(f"Nombre de bits pour le réseau {Nb_bits_reseau}")
print(f"Nombre de bits pour les hôtes {Nb_bits_hotes}")
print(f"Nombre total d'adresses {Nb_adresses}")
print(f"Nombre d'hôtes utilisables {Nb_hotes_util}")