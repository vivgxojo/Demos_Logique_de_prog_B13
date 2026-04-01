lignes = [
    "GigabitEthernet0/0  192.168.1.1   YES  manual  up    up",
    "GigabitEthernet0/1  10.0.0.1      YES  manual  up    up",
    "GigabitEthernet0/2  unassigned    YES  unset   down  down",
    "Loopback0           172.16.0.1    YES  manual  up    up",
]
print("--- État des interfaces ---")
print("Interface                 IP                 État")
print("-" * 55)
# pour chaque ligne dans la liste
for ligne in lignes:
    ls_donnes = ligne.split(" ")
    # tant qu'il reste des case vides dans la liste
    while "" in ls_donnes:
        ls_donnes.remove("") # supprimer les case vide
    #print(ls_donnes)
    interface = ls_donnes[0]
    ip = ls_donnes[1]
    if ls_donnes[-1] == "up":
        etat = "Active"
    else:
        etat = "Inactive"
    print(f"{interface:<26}{ip:<19}{etat:<10}")