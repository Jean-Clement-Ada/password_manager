# import hashlib
# import secrets

# pinceDeSel = secrets.token_hex(64)

# mdp = input("qu’est-ce que c’est ton mot de passe ? : ")

# algoChiffre = hashlib.sha3_512((mdp + pinceDeSel).encode())
# hash = algoChiffre.hexdigest()
# print(hash)
# fichierTopSecret = open("mesMotsDePasse", "a")
# fichierTopSecret.write(hash + "\n")
# fichierTopSecret.close()

import bcrypt

mdp = input("qu’est-ce que c’est ton mot de passe ? : ").encode()
print(mdp)

pinceDeSel = bcrypt.gensalt()
algoChiffre = bcrypt.hashpw(mdp, pinceDeSel)
print(algoChiffre)

fichierTopSecret = open("mesMotsDePasse", "a")
fichierTopSecret.write(algoChiffre.decode()+ "\n")
fichierTopSecret.close()


mdpVerif = input("Le mot de passe à vérifier : ").encode()
print(mdpVerif)

result = bcrypt.checkpw(mdpVerif, algoChiffre)

print(result)