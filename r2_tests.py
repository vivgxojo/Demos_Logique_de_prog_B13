from r2_fonction import *

print(verifier_acces([], "0.0.0.0"))
print(verifier_acces(["0.0.0.0"], "1.1.1.1"))
print(verifier_acces(["1.1.1.1"], "1.1.1.1"))
print(verifier_acces(["0.0.0.0", "1.1.1.1"], "1.1.1.1"))
print(verifier_acces(["0.0.0.0", "1.1.1.1"], "2.2.2.2"))