(actual,orig,dest)=(0,1,1)

def voirInventaire():
	print(f"\nContenu inventaire :")
	for item in inventaire:
		print(f"{item} : {inventaire[item]}")

def voirFichePerso():
	print(f"\nFiche personnage : ")
	for competence in joueur:
		print(f"{competence} : {joueur[competence]}")
		
def acheter(actual):
	o,p=vendeur[actual]
	if inventaire["argent"]>p:
		inventaire["argent"]=inventaire["argent"]-p
		if o not in inventaire:
			inventaire[o]=1
		else:
			inventaire[o]+=1
		print(f"Achat validé : 1 {o}")
	else:
		print(f"Argent manquant, achat annulé")
		
def combattre(actual):
	(cn,cv,ca,cd,ce)=combats[actual]
	print(f"Début du combat contre {cn}")
	while(joueur["vie"]>0 and cv>0):
		ans=input("Attaquer?\nDéfendre?  ")
		if (ans=="attaque"):
			cv-=(joueur["attaque"]-cd)
			joueur["vie"]-=(ca-joueur["défense"])
		else:
			joueur["vie"]-=(ca-joueur["défense"])
		print(f'joueur : {joueur["vie"]} points de vie')
		print(f"{cn} : {cv} points de vie")
	if(cv<=0):
		print(f"Combat réussi, {ce} points d'XP")
		joueur["exp"]+=ce
		goto(actual,orig,actual,dest)
	if(joueur["vie"]<=0):
		print("GAME OVER")
		exit()

def goto(x,orig,actual,dest):
	basic={-1:voirFichePerso,-2:voirInventaire,-3:lambda:acheter(actual),-4:lambda:combattre(actual)}
	if x in basic:
		basic[x]()
	else:
		actual= x
		_,t,a = textes[x]
		print(f"\n{t}")
		c = input(">> ")
		orig=actual
		if c in a:
			dest = a[c]
			goto(a[c],orig,actual,dest)
		else:
			dest=actual
	goto(actual,orig,actual,dest)

def main():
	(actual,orig,dest)=(0,1,1)
	while True :
		goto(actual,orig,actual,dest)

inventaire={
	"argent":50,
	"épée rouillée":1,
	"petit bouclier":1,
}

joueur={
	"vie":20,
	"attaque":5,
	"défense":5,
	"exp":0
}

vendeur={
	4:("couronne",20)
}

combats={#Nom, vie, attaque, défense,exp
	4:("Vendeur",6,6,3,15)
}

textes={
	0:(0,"TITRE AVENTURE\n Débuter l'aventure?",{"commencer":1,"démarrer":1,"débuter":1,"oui":1}),
	1:(1,"Bienvenue.\n Allez au nord.\n Aller à l'est\n Aller au sud-ouest",{"inventaire":-2,"joueur":-1,"nord":2,"est":3,"sud-ouest":4,"so":4}),
	2:(2,"Vous voici au nord.\n Allez au sud.\n Aller à l'ouest",{"inventaire":-2,"joueur":-1,"sud":1,"ouest":3}),
	3:(3,"Vous avez choisi l'est.\n Allez au nord-ouest.\n Aller à l'ouest",{"inventaire":-2,"joueur":-1,"nord-ouest":2,"est":1,"no":2}),
	4:(4,"Rue de l'horloge. Vendeur de couronnes, 20 pièces.\n Acheter?\n Combattre?\nRevenir sur ses pas?",{"achat":-3,"combat":-4,"inventaire":-2,"joueur":-1,"revenir":1})
}

main()
