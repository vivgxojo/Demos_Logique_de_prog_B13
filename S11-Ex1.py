"""
DEMANDER ip
ls_octets = SÉPARER ip
AFFICHER "Analyse..."
POUR nb d'octets
    AFFICHER "Octet", no, octet
somme = somme de ls_octets
AFFICHER somme
"""
ip = input("Entrez une adresse IP (ex: 192.168.1.10) : ")
ls_octets = ip.split(".")
print("--- Analyse de l'adresse IP ---")
for i in range(len(ls_octets)):
    print("Octet", i+1, ":", ls_octets[i])
    ls_octets[i] = int(ls_octets[i])
somme = sum(ls_octets)
print("Somme des octets :", somme)