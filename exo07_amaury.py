#!/usr/local/bin/python3.10
import math
import random
# Choisir un nombre entre 0 et 49
g  = input("Choisissez une somme entre 50 et 1000 : ")
while True:
    try:
        golds = int(g)
        if golds >= 50 and golds <= 1000:
            price = 50
            game = input("Voulez-vous jouer ? oui ou non ")
            print("Chaque manche vous coutera 50 golds")
            if game.lower() == "oui":
                print("Vous avez une reserve de", golds, "golds")
                val = input("Choisissez un nombre entre 0 et 49 : ")
                while True:
                    try:
                        choice=int(val)
                        if choice < 50 and choice > 0:
                            ball = random.randrange(50)
                            if choice % 2 == 0:
                                choiceColor = "noir"
                            else:
                                choiceColor = "rouge"
                            if ball % 2 == 0:
                                ballColor = "noir"
                            else:
                                ballColor = "rouge"
                                   
                            if choice == ball:
                                gain = price*3
                                g = golds = math.ceil(golds + gain)
                                print("OMG vous avez trouvé le bon numéro !!!")
                                print("vous avez gagné : ", gain)
                                print("Vous possédez encore ",golds,"golds")
                                break
                                
                            elif ballColor == choiceColor:
                                gain = price*0.5
                                g = golds = math.ceil(golds - gain)
                                print(gain, golds)
                                print("Félicitation, Vous avez trouvé la bonne couleur : ", ballColor)
                                print("Nous vous redonnons : ", gain)
                                print("Vous possédez encore ", golds, "golds")
                                break
                            else:
                                g = golds = golds - price
                                print("Malheur, vous avez perdu !!!")                                
                                print("Vous possédez encore ", golds, "golds")
                                break
                        else:
                            print("Attention : Choisissez un nombre entre 0 et 49 compris")
                            val = input("Choisissez un nombre entre 0 et 49 : ")  
                       
                    except ValueError:
                        print("Attention : Choisissez un nombre entre 0 et 49 compris")
                        val = input("Choisissez un nombre entre 0 et 49 : ")   
            else:
                print("Nous sommes Navré de vous voir partir !")
                break
        elif golds<50:
            print("Vous n'avez plus assez de crédit, vueillez quitter les lieux !!!")
            break
        else:
            print("ERREUR !!! Choisissez une somme entre 10 et 1000")
            g = input("Choisissez une somme entre 50 et 1000 : ")
    except ValueError:
        print("ERREUR !!! Choisissez une somme entre 10 et 1000")
        g = input("Choisissez une somme entre 50 et 1000 : ")
   
   

