def anayler_trafic(ls_debits, seuil = 100):
    """
    Analyse une liste de débits selon un seuil critique
    Calcule  :
    Le nombre de mesures
    Le débit minimum et maximum (calculés manuellement)
    La moyenne des débits
    Le nombre de mesures dépassant le seuil
    :param ls_debits: Liste de débits
    :param seuil: seuil critique
    :return: nb de mesures de débit, débit min, débit max, moyenne, nb de débit > le seuil
    """
    nb_debit = len(ls_debits)
    debit_min = ls_debits[0]
    debit_max = ls_debits[0]
    moyenne = sum(ls_debits)/nb_debit
    nb_depassement = 0
    for mesure in ls_debits:
        if mesure < debit_min:
            debit_min = mesure
        if mesure > debit_max:
            debit_max = mesure
        if mesure > seuil:
            nb_depassement += 1
    return nb_debit, debit_min, debit_max, moyenne, nb_depassement
# Programme principal
ls_debits = []
print("=== Analyseur de trafic réseau ===")
while True:
    debit = input("Débit (Mbps) : ")
    if debit == "fin":
        break
    ls_debits.append(float(debit))
print()
seuil = 100 # ou int(input("Seuil critique (Mbps) : "))
print("Seuil critique (Mbps) :", seuil)
print()
nb_debit, debit_min, debit_max, moyenne, nb_depassement = anayler_trafic(ls_debits) # , seuil optionnel
print("--- Rapport d'analyse ---")
print("Nombre de mesures : ", nb_debit)
print("Débit minimum     : ", debit_min, "Mbps")
print("Débit maximum     : ", debit_max, "Mbps")
print("Débit moyen       : ", moyenne,"Mbps")
print("Dépassements      : ",nb_depassement,"mesure(s) au-dessus de", seuil, "Mbps")
print("--- Visualisation ---")
for i in range(len(ls_debits)):
    d = ls_debits[i]
    nb_tirets = int(d/10)
    alerte = ""
    if d > seuil:
        alerte = "⚠"
    print(f"M{i+1}" + "-" * nb_tirets + f"{d:.1f} Mbps {alerte}")