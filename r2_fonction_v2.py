def verifier_acces(blacklist, liste_ip):
    """
    Vérifier si les adresses ip ont accès
    :param blacklist: liste d'adresses malveillantes
    :param liste_ip: liste d'adresses ip à vérifier
    :return: nombre d'adresses ip autorisées et nombre d'adresses ip refusées
    """
    nb_autorises = 0
    nb_refuses = 0
    for ip in liste_ip:
        if ip in blacklist:
            print(f"ACCÈS REFUSÉ  — {ip} est dans la blacklist.")
            nb_refuses += 1
        else:
            print(f"ACCÈS AUTORISÉ  — {ip} n'est pas dans la blacklist.")
            nb_autorises += 1
    return nb_autorises, nb_refuses

# Programme principal
blacklist = ["192.168.1.50", "10.0.0.99", "172.16.5.1", "192.168.100.200", "10.10.10.10"]
print("=== Vérification ACL - Pare-feu ===")
print(f"Blacklist chargée : {len(blacklist)} adresses bloquées.")
print()
ls_ip = []
while True:
    ip = input("Entrez une adresse IP à vérifier (ou 'fin') : ")
    if ip == "fin":
        break
    ls_ip.append(ip)
    print()
if len(ls_ip) == 0:
    print("Aucune adresse vérifiée.")
else:
    nb_autorises, nb_refuses = verifier_acces(blacklist, ls_ip)
    print("--- Résumé ---")
    print("Adresses vérifiées : ", len(ls_ip))
    print("Accès refusés      : ", nb_refuses)
    print("Accès autorisés    : ", nb_autorises)