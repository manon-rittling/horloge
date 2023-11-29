import time
import keyboard

heure = (23, 59, 57)
alarme = (0, 0, 0)
en_pause = False

def regler_alarme(heure, alarme):
    if alarme == heure:
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

def afficher_heure(heure, format_choisi):
    nouvelle_heure = list(heure)
    h, minute, seconde = nouvelle_heure

    while True:
        time.sleep(1)
        if 0 <= h < 24 and 0 <= minute < 60 and 0 <= seconde < 60:
            seconde = (seconde + 1) % 60
            if seconde == 0:
                minute = (minute + 1) % 60
                if minute == 0:
                    h = (h + 1) % 24

            regler_alarme(alarme, (h, minute, seconde))
            am_pm(h, minute, seconde, format_choisi)

            if keyboard.is_pressed("space"):
                global en_pause
                en_pause = not en_pause
                if en_pause:
                    print("En pause. Appuyez sur Entrée pour reprendre...")
                    input()  # Attendre que l'utilisateur appuie sur Entrée pour reprendre
                    print("Reprise...")
                else:
                    print("Reprise...")

format_choisi = input("Choisissez le format (24h ou am/pm): ")
afficher_heure(heure, format_choisi)


