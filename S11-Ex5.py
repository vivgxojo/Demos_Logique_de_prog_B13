"""
interfaces = [...]
AFFICHER entête
POUR CHAQUE interface
    AFFICHER interface
    REMPLACER ...
    AFFICHER interface
    SI interface COMMANCE PAR "Gi"
        type = "Gigabit"
    SINON SI interface COMMANCE PAR "Fa"
        type = "Fast
    SINON
        type = "Autre
    AFFICHER type
"""
interfaces = [
    "GigabitEthernet0/0",
    "GigabitEthernet0/1",
    "FastEthernet1/0",
    "Serial0/0/0",
    "Gi0/2",
    "Fa2/1",
    "Abcd2/1"
]

print("""--- Normalisation des interfaces ---
Nom original           Nom normalisé Type
--------------------------------------------------""")
for interface in interfaces:
    i = interface.index("/")-1
    int_norm = interface[:2] + interface[i:]
    if interface[0:2] == "Gi":
        #int_norm = interface.replace("GigabitEthernet", "Gi")
        type = "Gigabit"
    elif interface[0:2] == "Fa":
        #int_norm = interface.replace("FastEthernet", "Fa")
        type = "Fast"
    else:
        #int_norm = interface.replace("Serial", "Se")
        type = "Autre"
    print(f"{interface:<23}{int_norm:<14}{type}")