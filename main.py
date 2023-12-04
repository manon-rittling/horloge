import time
import os


heure = (16,59,57)
alarme=(17,0,0)

def afficher_heure(heure): 
    
    nouvelle_heure = list(heure) #Vous convertissez le tuple heure en liste nouvelle_heure pour permettre la modification des valeurs.
    h, minute, seconde = nouvelle_heure  #Vous extrayez les heures, minutes et secondes de la liste pour pouvoir les manipuler individuellement.

    

    while True:
        
        time.sleep(1) #introduit un délai d'une seconde entre chaque itération de la boucle, ce qui simule un écoulement du temps réaliste dans votre programme.
        if 0 <= h < 24 and 0 <= minute < 60 and 0 <= seconde < 60: # Vérification que l'heure, les minutes et les secondes sont dans des plages valides
            # Mettez à jour l'heure en ajoutant une seconde
            seconde = (seconde + 1) % 60  #Si les secondes dépassent 59, elles sont remises à zéro (modulo 60)
            if seconde == 0: # Si les secondes sont remises à zéro (c'est-à-dire qu'elles atteignent 60)
                minute = (minute + 1) % 60 # Ajoute une minute et remet à zéro si elle dépasse 59
                if minute == 0:
                    h = (h + 1) % 24 # Si les minutes sont remises à zéro (c'est-à-dire qu'elles atteignent 60)
                    os.system("pause")
                    
                
                 
            regler_alarme(alarme, (h, minute, seconde))
            
            am_pm(h, minute, seconde, format_choisi)
            
format_choisi = input("Choisissez le format (24h ou am/pm): ") #Vous demandez à l'utilisateur de choisir entre le format 24h et am/pm et stockez la réponse dans la variable format_choisi

            
def regler_alarme(heure, alarme): #Définition de la fonction regler_alarme qui imprime un message si l'alarme correspond à l'heure.
        if alarme == heure :
            print("C'est l'heure du réveil")

def am_pm(h, minute, seconde, format_choisi): #Début de la définition de la fonction am_pm pour afficher l'heure au format 24h ou am/pm.
    if format_choisi.lower() == "24h":
        heure_test = f"{h:02d}:{minute:02d}:{seconde:02d}"
        print(heure_test, end="\r")
    elif format_choisi.lower() == "am/pm": # Si le format choisi est "am/pm"
        suffixe = "AM" # Si le format choisi est "am/pm"
        if h >= 12:
            suffixe = 'PM'  # Si l'heure est supérieure à 12, ajuste l'heure en format 12 heures
        if h > 12:
            h -= 12
        elif h == 0:  # Si l'heure est 0, ajuste l'heure à 12 pour le format 12 heures
            h = 12

        heure_test=f'{h:02d}:{minute:02d}:{seconde:02d} {suffixe}'
        print(heure_test, end="\r")
    else:
        print("Format non reconnu. Veuillez choisir entre '24h' ou 'am/pm':")

afficher_heure(heure)

                
     
     





    
    
   



    
    


