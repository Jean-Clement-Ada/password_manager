import bcrypt

#ask for a password
mdp = input("quel est votre mot de passe ? : ").encode()
print(mdp)

#use bcrypt salt and hash
pinceDeSel = bcrypt.gensalt()
algoChiffre = bcrypt.hashpw(mdp, pinceDeSel)
print(algoChiffre)

#create a file with the bcrypt result
fichierTopSecret = open("mesMotsDePasse", "a")
fichierTopSecret.write(algoChiffre.decode())#+ "\n") #utiliser le fichier 'mesMotsDePasse' ne fonctionne pas avec "\n" pour paser à la ligne car bcyrpt.checkpw en tient compte et renvoi 'False'
fichierTopSecret.close()

#ask for a new password
mdpVerif = input("Le mot de passe à vérifier : ").encode()
print(mdpVerif)

#compare the new password with the hash
result = bcrypt.checkpw(mdpVerif, algoChiffre)

print(result)