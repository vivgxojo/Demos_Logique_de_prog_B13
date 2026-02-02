age = -1
if age > 70:
    print("Vieux")
elif 70 >= age >= 18: # and
    print("Adulte")
elif age < 18 and age >= 0:
    print("Enfant")
else:
    print("Erreur")