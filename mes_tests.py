from fonctions import *

print("Tests pour saluer_quelqun: --------------------")
saluer_quelqun("Maryse")
saluer_quelqun("")
saluer_quelqun(1)

print("Tests pour salutation_personnalise: --------------------")
salutation_personnalise("Maryse")
salutation_personnalise("", "")
salutation_personnalise(1, "français")
salutation_personnalise(1, "anglais")
salutation_personnalise(1, "espagnol")
salutation_personnalise(1, )

print("Tests pour additionner: --------------------")
print(additionner(0,1))
print(additionner(1,1))
print(additionner(-1,1))
print(additionner(-1000000,1))
print(additionner(1000000,1))
print(additionner(0.5,1))
#print(additionner("allo",1))
#print(additionner())
print(additionner(1,0))
print(additionner(1,1))
print(additionner(1,-1))
print(additionner(1,-1000000))
print(additionner(1,1000000))
print(additionner(1,0.5))
#print(additionner(1,"allo"))
#print(additionner(1))


print("Tests pour additionner_soustraire: --------------------")
ls_nombres = [0, 1, -1, -1000000, 1000000, 0.5]
print("Nombre de valeurs à tester", len(ls_nombres))
for i in range(len(ls_nombres)):
    print(addtionner_soustraire(ls_nombres[i], 1))
for i in range(len(ls_nombres)):
    print(addtionner_soustraire(1,ls_nombres[i]))