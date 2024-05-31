import bcrypt

with open('mesMotsDePasse', 'r') as mdp:
  
  #read and encode the document in bytes to use bcrypt
  mdpExtract = mdp.read().encode()
  print(mdpExtract)

  mdpVerif = input("le mot de passe à vérifier : ").encode()
  print(mdpVerif)

  #compare the new password with the hash in the document 'mesMotsDePasse'
  result = bcrypt.checkpw(mdpVerif, mdpExtract)

  print(result)


# todo :  - organiser le fichier texte pour séparer les entrées
#         - pouvoir comparer plusieurs entrées pour vérifier si un mot de passe stocké correspond (boucle for)
#         - chiffrer le fichier texte lui-même pour retrouver les mots de passe en clair à l’intérieur
#         - interface graphique
#
#   for i in mdp:
#     bcrypt.checkpw(mdpVerif, mdpExtract)
#     print(i)
