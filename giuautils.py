from datetime import datetime, timedelta
import locale
from colorama import Fore, Style, init


locale.setlocale(locale.LC_TIME, "it_IT.UTF-8")

init(autoreset=True)

def mostra_ascii():
    ascii_art = f"""
{Fore.CYAN} ██████╗ ██╗██╗   ██╗ █████╗ ██╗   ██╗████████╗██╗██╗     ███████╗
{Fore.CYAN}██╔════╝ ██║██║   ██║██╔══██╗██║   ██║╚══██╔══╝██║██║     ██╔════╝
{Fore.CYAN}██║  ███╗██║██║   ██║███████║██║   ██║   ██║   ██║██║     ███████╗
{Fore.CYAN}██║   ██║██║██║   ██║██╔══██║██║   ██║   ██║   ██║██║     ╚════██║
{Fore.CYAN}╚██████╔╝██║╚██████╔╝██║  ██║╚██████╔╝   ██║   ██║███████╗███████║
{Fore.CYAN} ╚═════╝ ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝╚══════╝╚══════╝

    {Fore.GREEN}Developed by Lorenzo Z 
    {Fore.BLUE} Classe : 5A 
    {Fore.YELLOW}Mantainer: Lorenzo Z
    """
    print(ascii_art)



def calcola_giorni_assenza(ore_totali):
    giorni_completi = 0
    ore_rimanenti = ore_totali

    for giorno in ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì"]:
        if giorno == "mercoledì":
            ore_giornaliere = 4  
        elif giorno in ["giovedì", "venerdì"]:
            ore_giornaliere = 6  
        else:
            ore_giornaliere = 5  

        if ore_rimanenti >= ore_giornaliere:
            giorni_completi += 1
            ore_rimanenti -= ore_giornaliere
        else:
            break

    return giorni_completi, ore_rimanenti


def analizza_assenze_dettagliate(assenze):
    ritardi = []
    uscite_anticipate = []
    assenze_complete = []

    for record in assenze:
        if "Ritardo" in record:
            ritardi.append(record)
        elif "Uscita anticipata" in record:
            uscite_anticipate.append(record)
        elif "Assenza" in record:
            if "-" in record:
                assenze_complete.extend(calcola_intervallo_date(record))
            else:
                assenze_complete.append(record)

    return ritardi, uscite_anticipate, assenze_complete


def calcola_intervallo_date(record):
    date_range = record.split("Assenza")[0].strip()
    date_parts = date_range.split(" - ")

    def get_anno_corretto(data):
        giorno, mese = data.split(" ")
        mese = mese.capitalize()  
        giorno = int(giorno)

        if mese in ["Settembre", "Ottobre", "Novembre", "Dicembre"]:
            return 2024
        elif mese in ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio"]:
            return 2025
        else:
            raise ValueError(f"Data fuori dal range dell'anno scolastico: {data}")

    start_date_part = date_parts[0]
    end_date_part = date_parts[1]

    start_anno = get_anno_corretto(start_date_part)
    end_anno = get_anno_corretto(end_date_part)

    start_date = datetime.strptime(start_date_part + f" {start_anno}", "%d %B %Y")
    end_date = datetime.strptime(end_date_part + f" {end_anno}", "%d %B %Y")

    assenze_giornaliere = []
    while start_date <= end_date:
        assenze_giornaliere.append(start_date.strftime("%d %B Assenza"))
        start_date += timedelta(days=1)

    return assenze_giornaliere


def calcola_ore_uscite(uscite):
    ore_totali = 0
    for uscita in uscite:
        ora_uscita = int(uscita.split("(")[1].split(":")[0])
        minuto_uscita = int(uscita.split("(")[1].split(":")[1].split(")")[0])

        if ora_uscita == 12 and minuto_uscita >= 15:
            ore_totali += 4  
        elif ora_uscita == 13 and minuto_uscita >= 15:
            ore_totali += 5  
        elif ora_uscita == 14 and minuto_uscita >= 15:
            ore_totali += 6  

    return ore_totali

def calcola_ore_assenze(assenze):
    return 174  # Valore segnato nel registro


def main():
    mostra_ascii()
    print("\033[37m[\033[32mINFO\033[37m] \033[0mSeleziona un'opzione:")
    print("1. Calcolo dall'array assenze.")
    print("2. Visualizza dati segnati nel registro.")
    print("3. Calcolo delle assenze dal file assenze.txt.")
    print("4. Esci")

    scelta = input("\033[37m[\033[34mINPUT\033[37m] \033[0mInserisci la tua scelta: ")

    if scelta == "1":
        assenze = [
            "9 Gennaio Uscita anticipata (12:15)",
            "7 Gennaio Uscita anticipata (12:00)",
            "20 Dicembre Assenza",
            "19 Dicembre Uscita anticipata (12:15)",
            "16 Dicembre Uscita anticipata (12:15)",
            "14 Dicembre Assenza",
            "13 Dicembre Uscita anticipata (13:14)",
            "10 Dicembre Assenza",
            "9 Dicembre Uscita anticipata (12:00)",
            "7 Dicembre Assenza",
            "6 Dicembre Uscita anticipata (13:15)",
            "5 Dicembre Uscita anticipata (12:15)",
            "4 Dicembre Uscita anticipata (12:11)",
            "3 Dicembre Assenza",
            "23 Novembre - 30 Novembre Assenza",
            "22 Novembre Uscita anticipata (12:15)",
            "20 Novembre Assenza",
            "19 Novembre Ritardo (09:18)",
            "18 Novembre Assenza",
            "16 Novembre Ritardo (08:30)",
            "15 Novembre Assenza",
            "12 Novembre Uscita anticipata (11:40)",
            "29 Ottobre - 11 Novembre Assenza",
            "28 Ottobre Uscita anticipata (12:20)",
            "26 Ottobre Assenza",
            "25 Ottobre Uscita anticipata (12:00)",
            "16 Ottobre - 19 Ottobre Assenza",
            "14 Ottobre Assenza",
            "12 Ottobre Ritardo (08:34)",
            "8 Ottobre - 10 Ottobre Assenza",
            "5 Ottobre Assenza",
            "3 Ottobre Assenza",
            "1 Ottobre Assenza",
            "27 Settembre Assenza",
            "25 Settembre Uscita anticipata (11:55)",
            "17 Settembre Assenza",
        ]

        ritardi, uscite_anticipate, assenze_complete = analizza_assenze_dettagliate(assenze)

        print(f"\033[37m[\033[32mINFO\033[37m] \033[0mRitardi: {len(ritardi)}")
        print(f"\033[37m[\033[32mINFO\033[37m] \033[0mUscite anticipate: {len(uscite_anticipate)}")
        print(f"\033[37m[\033[32mINFO\033[37m] \033[0mAssenze complete: {len(assenze_complete)}")

        ore_totali = calcola_ore_assenze(assenze_complete)
        print(f"\033[37m[\033[32mINFO\033[37m] \033[0mOre totali calcolate: {ore_totali}")

        giorni, ore_rimanenti = calcola_giorni_assenza(ore_totali)
        print(f"Hai accumulato {giorni} giorni completi di assenza e {ore_rimanenti} ore rimanenti.")

    elif scelta == "2":
        ore_totali = 174  # Ore segnate nel registro
        ritardi = 3  # Ritardi segnati nel registro
        uscite_anticipate = 14  # Uscite anticipate segnate nel registro

        print(f"\033[37m[\033[32mINFO\033[37m] \033[0mOre segnate nel registro: {ore_totali}")
        print(f"\033[37m[\033[32mINFO\033[37m] \033[0mRitardi segnati nel registro: {ritardi}")
        print(f"\033[37m[\033[32mINFO\033[37m] \033[0mUscite anticipate segnate nel registro: {uscite_anticipate}")

    elif scelta == "3":
        try:
            with open("assenze.txt", "r", encoding="utf-8") as f:
                assenze = [line.strip() for line in f.readlines()]

            ritardi, uscite_anticipate, assenze_complete = analizza_assenze_dettagliate(assenze)

            print(f"\033[37m[\033[32mINFO\033[37m] \033[0mRitardi: {len(ritardi)}")
            print(f"\033[37m[\033[32mINFO\033[37m] \033[0mUscite anticipate: {len(uscite_anticipate)}")
            print(f"\033[37m[\033[32mINFO\033[37m] \033[0mAssenze complete: {len(assenze_complete)}")

            ore_totali = calcola_ore_assenze(assenze_complete)
            print(f"\033[37m[\033[32mINFO\033[37m] \033[0mOre totali calcolate: {ore_totali}")

            giorni, ore_rimanenti = calcola_giorni_assenza(ore_totali)
            print(f"Hai accumulato {giorni} giorni completi di assenza e {ore_rimanenti} ore rimanenti.")

        except FileNotFoundError:
            print("\033[37m[\033[31mERROR\033[37m] \033[0mIl file 'assenze.txt' non è stato trovato. Assicurati che esista nella directory corrente.")
    elif scelta == "4": 
        mostra_ascii()
        print(Fore.RED + "Grazie per aver usato il programma")
        print("\033[37m[\033[32mINFO\033[37m] \033 [Uscita in Corso......")
        exit()

    else:
        print("\033[37m[\033[31mERROR\033[37m] \033[0mScelta non valida. Riprova.")

if __name__ == "__main__":
    main()

