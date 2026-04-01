ip = " 255.255.224.0 "
ip = ip.strip() # enlever les espaces au début et à la fin
ls_octets = ip.split(".") # str -> liste
print(ls_octets)
print("-".join(ls_octets)) # liste -> str
print("Nombre de caractères:", len(ip))
print("Nombre d'octets:", len(ls_octets))
nom = input("NOM:").strip()
print(len(nom))
print(nom.upper()) # en majuscules
print(nom.lower()) # en minuscules
print(nom.title()) # première lettre des mots en majuscules
print(nom.capitalize()) # première lettre de la phrase en majuscule
ip = ip.replace(".", ":") # remplace un caractère par un autre
print(ip)
ip = ip.replace(":", "")  # supprimer les caractères
print(ip)
print(ip[-1]) # le dernier caractère de la chaine
print(ip[0:3]) # les 3 premier caractères [0,3[
print(ip[6:9]) #[6,9[
indice = ip.find("4") # trouver l'indice d'un caractère
print(indice)
i_espace = nom.find(" ") # trouver l'indice de l'espace
print(i_espace)
count_255 = ip.count("255")
print(count_255)
ip1 = "255.255.4.1"
ip2 = "255.255.255.1"
ip3 = "255.128.001.001"
ls_ip1 = ip1.split(".")
ls_ip2 = ip2.split(".")
ls_ip3 = ip3.split(".")
print(f"{ls_ip1[0]:>3} . {ls_ip1[1]:>3} . {ls_ip1[2]:>3} . {ls_ip1[3]:>3}")
print(f"{ls_ip2[0]:>3} . {ls_ip2[1]:>3} . {ls_ip2[2]:>3} . {ls_ip2[3]:>3}")
print(f"{ls_ip3[0]:>3} . {ls_ip3[1]:>3} . {ls_ip3[2]:>3} . {ls_ip3[3]:>3}")