import S3_1_Fonction_Ports

# Demander le numéro de port à l'utilisateur
port = int(input("Entrez un numéro de port (0-65535) : "))
categorie = S3_1_Fonction_Ports.analyser_port(port)
# Afficher le résultat
print(f"Le port {port} appartient à la catégorie : {categorie}")