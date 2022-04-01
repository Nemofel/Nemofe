import random

nombreAleatoire = random.randint(1,123)

choixUtilisateur = -1 

compteur = 0

compteur = compteur+1

while choixUtilisateur != nombreAleatoire :

	choixUtilisateur = int(input("choisit un nombre ?\n"))
		 
	compteur = compteur +1

	if nombreAleatoire == choixUtilisateur :
		print("T'es le BOSS")
	elif nombreAleatoire > choixUtilisateur :
		print("Essaie plus grand")

	else :
		print("Essaie plus petit")



print("Tu as avez reussie en ", compteur)
