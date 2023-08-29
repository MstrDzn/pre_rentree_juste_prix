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
def verif(entreef,prixf): 
    if entreef==prixf:
        print("Bravo")
        return False
    else:
        if entreef>prixf:
            print("Trop élevé")
        else:
            print("Pas assez")
        return True


while state==True:
    count+=1
    if count==6:
        print ("Perdu")
        break
    try:
        entree=int(input("Veuillez saisir votre prix:"))
    except:
        print("La valeur est incorrecte...")
    state=verif(entree,prix)
    

