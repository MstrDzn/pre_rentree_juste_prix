'''
- tirer au sort un prix
- choix du joueur
- si prix trouvé => message; sinon => indication
- si inférieur; pas assez, si supérieur trop
'''
from random import *

state=True
count=0
prix=randint(1,100)
while state==True:
    count+=1
    if count==6:
        print ("Perdu")
        break
    try:
        entree=int(input("Veuillez saisir votre prix:"))
    except:
        print("La valeur est incorrecte...")


    if entree==prix:
        print("Bravo")
        state=False
    else:
        if entree>prix:
            print("Trop élevé")
        else:
            print("Pas assez")