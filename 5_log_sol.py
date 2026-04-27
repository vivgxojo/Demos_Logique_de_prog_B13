def trier_logs(logs):
    infos = []
    warnings = []
    erreurs = []

    for ligne in logs:
        if ligne.startswith("[INFO]"):
            infos.append(ligne)
        elif ligne.startswith("[WARNING]"):
            warnings.append(ligne)
        elif ligne.startswith("[ERROR]"):
            erreurs.append(ligne)

    return infos, warnings, erreurs


def afficher_messages(titre, messages):
    print(f"=== {titre} ===")
    if len(messages) == 0:
        print(f"  Aucun {titre.lower()}.")
    else:
        for msg in messages:
            print(" ", msg)


def afficher_resume(infos, warnings, erreurs):
    print("\n=== Résumé ===")
    print("INFO    :", len(infos), "message(s)")
    print("WARNING :", len(warnings), "message(s)")
    print("ERROR   :", len(erreurs), "message(s)")

    if len(erreurs) > 2:
        print("\n*** ALERTE : plus de 2 erreurs détectées ! Intervention requise. ***")


# Programme principal
logs = [
    "[INFO]    10:00:01  Interface Gi0/0 is up",
    "[ERROR]   10:00:03  OSPF neighbor 10.0.0.2 went down",
    "[INFO]    10:00:05  BGP session established with 192.168.1.2",
    "[WARNING] 10:00:07  CPU usage at 87% on R1",
    "[ERROR]   10:00:09  Interface Gi0/1 link failure",
    "[INFO]    10:00:11  NTP sync successful",
    "[WARNING] 10:00:13  Memory usage above threshold on SW2",
    "[ERROR]   10:00:15  Authentication failed from 203.0.113.5",
]

infos, warnings, erreurs = trier_logs(logs)
print()
afficher_messages("Avertissements", warnings)
print()
afficher_messages("Erreurs", erreurs)
print()
afficher_resume(infos, warnings, erreurs)
print()