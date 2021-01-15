couleurs={}

def initPicross(typeP):
	nF=input("Nom du fichier? ")
	nbCol=int(input("Nombre de colonnes "))
	nbLig=int(input("Nombre de lignes "))
	if typeP in ("P1","p1"):
		var=0
	else:
		var=input("Nombre de nuances ")
	with open(nF,'w') as fic:
		fic.write(typeP.upper()+"\n"+str(nbCol)+" "+str(nbLig)+"\n")
		if var!=0:
			fic.write(var+"\n")
	createColours(typeP,couleurs)
	runPicross(couleurs,nF,nbCol,nbLig)

def createColours(typeP,couleurs):
	print("typeP colors  "+typeP)
	if typeP in ("P1","p1"):
		couleurs["n"]=1
		couleurs["b"]=0
	else:
		while(input("creer couleur ou sortir? ")!="sortir"):
			n=input("nom couleur")
			v=input("valeur couleur")
			couleurs[n]=v
	return couleurs

def runPicross(couleurs,nF,nbCol,nbLig):
	compt=0
	linae=1 
	with open(nF,'a') as fic:
		while True:
	
			if(compt == nbCol):
				fic.write("\n")
				compt=0
				linae=linae+1
			
			if (linae>nbLig):
				print("\n fichier terminé \n")
				exit(0)
		
			print("Ligne numéro ",linae)
			print("compteur vaut ",compt)
			ent=(input("ValeurCouleur : " ))
			valeur=int(ent[:-1])
			couleur=ent[-1:]
			
		
			compt=compt+valeur
			
			if couleur in couleurs:
				ligne=valeur*(str(couleurs[couleur])+" ")
			else:
				ligne=valeur*(str(couleur)+" ")
			fic.write(ligne)



def resumePicross():
	return None

def savePicross():
	return None

def main():
	state=input("Nouveau picross : n\nContinuer : r\n")
	if state=="n":
		typeP=input("Quel picross?\nNoir et blanc : P1\nNiveaux de gris : P2\nEn couleurs : P3\n")
		print(typeP)
		initPicross(typeP)
	else:
		resumePicross()


main()