# Valider un octet d'adresse IP entre 0 et 255
while True:
    try: # prévention
        octet = int(input("Entrez l'octet (0-255) : "))
        if octet >= 0 and octet <= 255: # validation d'interval
            break
        else:
            print("Erreur, l'octet doit être entre 0 et 255.")
    except: # gestion d'erreur
        print("Erreur, l'octet doit être un nombre entier.")

print("L'octet", octet, "est valide.")

# Gérer une division par 0 :
try:
    somme = int(input("Entrez la somme des notes "))
    nb = int(input("Entrez le nombre d'étudiants "))
    moyenne = somme / nb
    print(moyenne)
except:
    print("Une erreur est survenue.")