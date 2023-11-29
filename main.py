import time
import os


heure = (23,59,57)
alarme=(0,0,2)

def afficher_heure(heure):
    
    nouvelle_heure = list(heure) #Vous convertissez le tuple heure en liste nouvelle_heure pour permettre la modification des valeurs.
    h, minute, seconde = nouvelle_heure  #Vous extrayez les heures, minutes et secondes de la liste pour pouvoir les manipuler individuellement.

    print(f'{h:02d}:{minute:02d}:{seconde:02d}')

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
            
format_choisi = input("Choisissez le format (24h ou am/pm): ")

            
def regler_alarme(heure, alarme):
        if alarme == heure :
            print("C'est l'heure du réveil")

def am_pm(h, minute, seconde, format_choisi):
    if format_choisi.lower() == "24h":
        print(f"{h:02d}:{minute:02d}:{seconde:02d}")
    elif format_choisi.lower() == "am/pm":
        suffixe = "AM"
        if h >= 12:
            suffixe = 'PM'
        if h > 12:
            h -= 12
        elif h == 0:
            h = 12

        print(f'{h:02d}:{minute:02d}:{seconde:02d} {suffixe}')
    else:
        print("Format non reconnu. Veuillez choisir entre '24h' ou 'am/pm'.")

afficher_heure(heure)

                
     
     





    
    
   



    
    


