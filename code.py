code_1 = 200
code_2 = "404"
code_3 = 500
code_4 = "301"

# 1. afficher les types
print("Type du code 1:", type(code_1))
print("Type du code 2:", type(code_2))
print("Type du code 3:", type(code_3))
print("Type du code 4:", type(code_4))

# 2. convertir les chaines en entier
code_2 = int(code_2)
code_4 = int(code_4)
print("Type du code 2:", type(code_2))
print("Type du code 4:", type(code_4))

# 3 déterminer la catégorie : centaine
print("Catégorie du code 1:", code_1//100)
print("Catégorie du code 2:", code_2//100)
print("Catégorie du code 3:", code_3//100)
print("Catégorie du code 4:", code_4//100)