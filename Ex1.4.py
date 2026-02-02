# 4 : Déterminer si un numéro de port est valide
# Entrées : ports
port_1 = 80 #(HTTP)
port_2 = 65535 #(port maximum)
port_3 = 70000 #(invalide)
port_4 = -5 #(invalide)
port_5 = 22 #(SSH)

# Traitements : déterminer si c'est valide
port_1_valide = port_1 >= 0 and port_1 <= 65535

# Afficher les messages
print("Port 1 valide ?", port_1_valide)
print("Port 2 valide ?", port_2 >= 0 and port_2 <= 65535)

# Conditions
if port_3 >= 0 and port_3 <= 65535:
    print("Le port 3 est valide !")
else:
    print("Le port 3 n'est pas valide !")

if 0 <= port_4 <= 65535:
    print("Le port 4 est valide !")
else:
    print("Le port 4 n'est pas valide !")

port_5_valide = False #équivalent du else
if port_5 >= 0:
    port_5_valide = True
    if port_5 > 65535:
        port_5_valide = False
if port_5_valide:
    print("Le port 5 est valide !")
else:
    print("Le port 5 n'est pas valide !")