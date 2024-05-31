import bcrypt

with open('mesMotsDePasse', 'r') as mdp:
  print(mdp.read())

  pinceDeSel = bcrypt.gensalt()
  algohChiffre = bcrypt.hashpw(mdp, pinceDeSel)

mdpVerif = input("le mot de passe à vérifier : ").encode()

result = bcrypt.checkpw(mdpVerif, algoChiffre)

print(result)

# def verifPassword(mesMotsDePasse):
#   #fichierTopSecret = open("mesMotsDePasse", "r")
#   for i in fichierTopSecret:
#     bcrypt.checkpw(mdp, algoChiffre)
#     print(i)

# print(verifPassword(fichierTopSecret))
# print(fichierTopSecret.read())