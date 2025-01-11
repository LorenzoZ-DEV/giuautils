from colorama import Fore, Style
from tabulate import tabulate
import time
import sys

# Dizionario con i voti delle materie
voti = {
    "Italiano": [4.5, 4.5],
    "Storia": [4],
    "Inglese": [4.5],
    "Matematica": [6.5],
    "Informatica": [3.5, 3, 4, 5, 3.5],
    "Sistemi": [6.5],
    "Tecn. prog. sis.": [6, 4.5],
    "Gestione prog.": [6.5],
    "Sc. motorie": [8]
}

# Calcolo delle materie sotto la sufficienza
materie_sotto = [materia for materia, voti_materia in voti.items() if any(voto < 6 for voto in voti_materia)]

# Calcolo delle medie
medie_materie = {materia: sum(voti_materia) / len(voti_materia) for materia, voti_materia in voti.items()}

# Funzione per calcolare quanti voti servono per raggiungere la sufficienza
def calcola_voti_per_sufficienza(voti_materia):
    media_attuale = sum(voti_materia) / len(voti_materia)
    if media_attuale >= 6:
        return 0  # Già sufficiente
    somma_attuale = sum(voti_materia)
    n_voti = len(voti_materia)
    voti_necessari = 0
    while (somma_attuale + voti_necessari) / (n_voti + voti_necessari) < 6:
        voti_necessari += 1
    return voti_necessari

# Funzione per mostrare un'animazione durante l'attesa
def animazione_attesa(messaggio, durata):
    for _ in range(durata):
        for frame in "|/-\\":
            sys.stdout.write(f"\r{Fore.YELLOW}{messaggio} {frame}{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.2)
    sys.stdout.write("\r" + " " * len(messaggio) + "\r")

# ASCII art per diverse fasi e condizioni
def mostra_ascii_fase(fase):
    if fase == "menu_principale":
        print(Fore.CYAN + """
 ██████╗ ██╗██╗   ██╗ █████╗                    
██╔════╝ ██║██║   ██║██╔══██╗                   
██║  ███╗██║██║   ██║███████║                   
██║   ██║██║██║   ██║██╔══██║                   
╚██████╔╝██║╚██████╔╝██║  ██║                   
 ╚═════╝ ╚═╝ ╚═════╝ ╚═╝  ╚═╝                   
                                                
██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗ 
██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗
███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝
██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗
██║  ██║███████╗███████╗██║     ███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
""" + Style.RESET_ALL)
    elif fase == "materie_sotto":
        print(Fore.RED + """
██╗    ██╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗ 
██║    ██║██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝ 
██║ █╗ ██║███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
██║███╗██║██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║
╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
""" + Style.RESET_ALL)
    elif fase == "tutto_ok":
        print(Fore.GREEN + """
 ██████╗ ██╗  ██╗
██╔═══██╗██║ ██╔╝
██║   ██║█████╔╝ 
██║   ██║██╔═██╗ 
╚██████╔╝██║  ██╗
 ╚═════╝ ╚═╝  ╚═╝
""" + Style.RESET_ALL)

# Menu principale
mostra_ascii_fase("menu_principale")
print("Scegli un'opzione:")
print("1. Visualizza la media attuale e le materie sotto la sufficienza")
print("2. Calcola quanti voti servono per la sufficienza e verifica se sei a rischio di non fare l'esame di stato")
scelta = input("Inserisci il numero della tua scelta (1 o 2): ")

if scelta == "1":
    if len(materie_sotto) > 0:
        mostra_ascii_fase("materie_sotto")
    else:
        mostra_ascii_fase("tutto_ok")

    print("\nMaterie sotto la sufficienza:")
    for materia in materie_sotto:
        print(f"{Fore.RED}{materia}{Style.RESET_ALL}")
    
    print("\nTabella delle medie:")
    table = []
    for materia, media in medie_materie.items():
        stato = f"{Fore.GREEN}Sufficiente{Style.RESET_ALL}" if media >= 6 else f"{Fore.RED}Insufficiente{Style.RESET_ALL}"
        table.append([materia, f"{media:.2f}", stato])
    print(tabulate(table, headers=["Materia", "Media", "Stato"], tablefmt="grid"))

elif scelta == "2":
    # Mostra animazione dinamica durante il calcolo
    animazione_attesa("Calcolo in corso", 5)

    # Mostra ASCII di conferma calcolo completato
    print(Fore.GREEN + """
██████╗ ███████╗ ██████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ 
██╔══██╗██╔════╝██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔═══██╗
██████╔╝█████╗  ██║     ██║   ██║██████╔╝█████╗  ██████╔╝██║   ██║
██╔══██╗██╔══╝  ██║     ██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██║   ██║
██║  ██║███████╗╚██████╗╚██████╔╝██║     ███████╗██║  ██║╚██████╔╝
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ 
""" + Style.RESET_ALL)

    # Costruisce i dati della tabella
    table = []
    for materia, voti_materia in voti.items():
        voti_necessari = calcola_voti_per_sufficienza(voti_materia)
        stato = "Sufficiente" if medie_materie[materia] >= 6 else "Insufficiente"
        table.append([materia, f"{medie_materie[materia]:.2f}", stato, voti_necessari])

    # Debug: verifica se i dati della tabella sono stati generati correttamente
    if len(table) == 0:
        print(Fore.RED + "Errore: Nessun dato trovato per costruire la tabella." + Style.RESET_ALL)
    else:
        print("\nCalcolo completato! Ecco i voti necessari per raggiungere la sufficienza:\n")
        # Stampa la tabella
        print(tabulate(table, headers=["Materia", "Media", "Stato", "Voti necessari"], tablefmt="grid"))



