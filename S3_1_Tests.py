from S3_1_Fonction_Ports import *

ls_ports = [-1, 0, 1023, 1024, 49151, 49152, 65535, 65536, "allo"]
for port in ls_ports:
    print(analyser_port(port))