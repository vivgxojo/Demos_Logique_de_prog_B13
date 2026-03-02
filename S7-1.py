# Générer les 8 adresses IP d'un sous-réseau /29
octet1 = input("Entrez le 1ier octet de l'adresse IP ")
octet2 = input("Entrez le 2e octet de l'adresse IP ")
octet3 = input("Entrez le 3e octet de l'adresse IP ")
octet4 = input("Entrez le 4e octet de l'adresse IP ")

for i in range(0, 8):
    adresse_ip = octet1 + "." + octet2 + "." + octet3 + "." + str(i)
    print(adresse_ip)