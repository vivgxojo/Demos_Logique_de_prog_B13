from S13_4 import *
#heure     0, 1,  2,  3, 4,  5,  6   ....
ls_cpu = [10, 2, 90, 91, 0, 15, 99] #...
ls_ram = [90, 4, 40, 50, 0, 91, 95]
moyenne_cpu, moyenne_ram, alertes = analyser_ressource(ls_cpu, ls_ram)
print(f"Moyenne d'utilisation du CPU : {moyenne_cpu:.1f}")
print(f"Moyenne d'utilisation de la RAM : {moyenne_ram:.1f}")
for alerte in alertes:
    print(alerte)

"""
Exemple de sortie attendue
Alerte intermédiaire : cpu utilisé à 91% à 3h.
Alerte intermédiaire : ram utilisé à 91% à 5h.
Alerte critique : cpu (99%) et ram (95%) dépassent 90% à 6h.
"""