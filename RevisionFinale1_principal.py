from RevisionFinale1_fonction import *
ls_ping = []
print("=== Test de stabilité de connexion ===")
for i in range(5):
    while True:
        try:
            temps = float(input(f"Ping {i+1} (ms) : "))
            if temps <= 0:
                print("Erreur : valeur négative refusée.")
            else:
                ls_ping.append(temps)
                break
        except:
            print("Erreur : entrez un nombre valide.")
moyenne, min, max, verdict = analyser_ping(ls_ping)
print("--- Résultats ---")
print(f"Ping minimum : {min} ms")
print(f"Ping maximum : {max} ms")
print(f"Moyenne      : {moyenne:.1f} ms")
print(f"Verdict      : {verdict}")
