# Catégories de ports
# Demander le no de port
port = int(input("Entrez le numéro de port : "))

# Déterminer la catégorie
categorie = None    # Initialiser la variable pour qu'elle existe
if 0 <= port <= 1023:
    categorie = "bien connus"
elif 1024 <= port <= 49151:
    categorie = "enregistrés"
elif 49152 <= port <= 65535:
    categorie = "dynamiques/privés"
else:
    print("Erreur : Port non valide")

# Afficher la catégorie
print("La catégorie est ports", categorie)