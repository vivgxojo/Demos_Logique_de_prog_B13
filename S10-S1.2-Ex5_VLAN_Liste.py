## Exercice 5 : Comprendre les types pour les numéros de VLAN

# Données (types mixtes)
ls_vlans = [10, "20", 100, "1005"]

# Affichage des types originaux
print("--- Types originaux ---")
for i in range(len(ls_vlans)):
    print("VLAN ", i+1, ":", ls_vlans[i], "- Type:", type(ls_vlans[i]))

# Conversion en int si nécessaire
ls_vlans[1] = int(ls_vlans[1])
ls_vlans[3] = int(ls_vlans[3])

print("\n--- Après conversion ---")
print("VLAN 2:", ls_vlans[1], "- Type:", type(ls_vlans[1]))
print("VLAN 4:", ls_vlans[3], "- Type:", type(ls_vlans[3]))

# Validation (VLAN valides: 1-4094)
print("\n--- Validation ---")
for i in range(len(ls_vlans)):
    vlan_i_valide = ls_vlans[i] >= 1 and ls_vlans[i] <= 4094
    print("VLAN", ls_vlans[i], "valide:", vlan_i_valide)

#vlan4_valide = ls_vlans[3] >= 1 and ls_vlans[3] <= 4094
#print("VLAN", ls_vlans[3], "valide:", vlan4_valide)

# Déterminer le type de VLAN
print("\n--- Type de VLAN ---")
for i in range(len(ls_vlans)):
    vlan_i_standard = ls_vlans[i] >= 1 and ls_vlans[i] <= 1005
    vlan_i_etendu = ls_vlans[i] >= 1006 and ls_vlans[i] <= 4094
    print("VLAN", ls_vlans[i], "- Standard:", vlan_i_standard, "- Étendu:", vlan_i_etendu)

# Vérifier si c'est un VLAN réservé
print("\n--- VLANs réservés ---")
for i in range(len(ls_vlans)):
    vlan_i_reserve = ls_vlans[i] == 1 or (ls_vlans[i] >= 1002 and ls_vlans[i] <= 1005)
    print("VLAN", ls_vlans[i], "réservé:", vlan_i_reserve)

# Résultats:
# VLAN 1: 10 (int) → valide, standard, non réservé
# VLAN 2: "20" (str) → 20 (int) → valide, standard, non réservé
# VLAN 3: 100 (int) → valide, standard, non réservé
# VLAN 4: "1005" (str) → 1005 (int) → valide, standard, réservé