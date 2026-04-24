from r2_fonction import *
"""
nb_ip_total = 0
nb_autorises = 0
nb_refuses = 0
TANT QUE VRAI
    DEMANDER ip
    SI ip = "fin"
        TERMINER BOUCLE
    nb_ip_total += 1
    acces = APPELER FONCTION verifier_acces(ip)
    SI acces
        AFFICHE "ACCÈS AUTORISÉ" 
        nb_autorises += 1
    SINON
    	AFFICHE "ACCÈS REFUSÉ" 
    	nb_refuses += 1
SI nb_ip_total = 0:
    AFFICHER "Aucune adresse vérifiée."
SINON
    AFFICHER resumé...        
"""
blacklist = ["192.168.1.50", "10.0.0.99", "172.16.5.1", "192.168.100.200", "10.10.10.10"]
nb_ip_total = 0
nb_autorises = 0
nb_refuses = 0
print("=== Vérification ACL - Pare-feu ===")
print(f"Blacklist chargée : {len(blacklist)} adresses bloquées.")
print()
while True:
    ip = input("Entrez une adresse IP à vérifier (ou 'fin') : ")
    if ip == "fin":
        break
    nb_ip_total += 1
    acces = verifier_acces(blacklist, ip)
    if acces:
        print(f"ACCÈS AUTORISÉ  — {ip} n'est pas dans la blacklist.")
        nb_autorises += 1
    else:
        print(f"ACCÈS REFUSÉ  — {ip} est dans la blacklist.")
        nb_refuses += 1
    print()
if nb_ip_total == 0:
    print("Aucune adresse vérifiée.")
else:
    print("--- Résumé ---")
    print("Adresses vérifiées : ", nb_ip_total)
    print("Accès refusés      : ", nb_refuses)
    print("Accès autorisés    : ", nb_autorises)