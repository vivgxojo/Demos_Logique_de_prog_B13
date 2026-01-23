ip1 = "192.168.1.100"
ip2 = "10.0.0.1"
ip3 = "172.16.254.1"

print("Type de ip1:", type(ip1))  

octets = ip1.split(".") # c'est quoi split ?
print("Octets de", ip1, ":", octets)  
print("Type de octets:", type(octets))  

premier_octet = octets[0]
dernier_octet = octets[3]
print("Premier octet:", premier_octet)  
print("Dernier octet:", dernier_octet)  

dernier_octet_int = int(dernier_octet)
print("Dernier octet en int:", dernier_octet_int) 
print("Type:", type(dernier_octet_int))  

est_pair = dernier_octet_int % 2 == 0
print("Le dernier octet est pair:", est_pair)  

print("\n--- IP2 ---")
octets2 = ip2.split(".")
print("Dernier octet de", ip2, ":", octets2[3])
est_pair2 = int(octets2[3]) % 2 == 0
print("Est pair:", est_pair2)  

print("\n--- IP3 ---")
octets3 = ip3.split(".")
print("Dernier octet de", ip3, ":", octets3[3])
est_pair3 = int(octets3[3]) % 2 == 0
print("Est pair:", est_pair3)  