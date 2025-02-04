from voti import Voti
from assenze import Assenze
from colorama import Fore, Style


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


def mostra_menu():
    print("\nScegli un'opzione:")
    print("1. Visualizza voti e medie")
    print("2. Aggiungi un nuovo voto")
    print("3. Rimuovi un voto")
    print("4. Visualizza assenze")
    print("5. Aggiungi assenze")
    print("6. Esci")


def main():
    mostra_ascii()  # Mostra l'ASCII art all'inizio
    voti = Voti()
    assenze = Assenze()
    assenze.aggiungi_assenze([
        "3 Febbraio Uscita anticipata (12:00)",
        "1 Febbraio Ritardo (08:27)",
        "1 Febbraio Uscita anticipata (12:15)",
        "31 Gennaio Assenza",
        "24 Gennaio Assenza",
        "25 Gennaio Assenza",
        "23 Gennaio Uscita anticipata (10:15)",
        "18 Gennaio Uscita anticipata (12:15)",
        "24 Gennaio Assenza",
        "22 Gennaio Assenza",
        "16 Gennaio Assenza",
        "14 Gennaio Assenza",
        "11 Gennaio Uscita anticipata (12:15)",
        "13 Gennaio Uscita anticipata (12:08)",
        "10 Gennaio Assenza",
        "9 Gennaio Uscita anticipata (12:15)",
        "7 Gennaio Ritardo (09:30)"
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
    ])

    while True:
        mostra_menu()
        scelta = input(f"{Fore.BLUE}Inserisci la tua scelta: {Style.RESET_ALL}")

        if scelta == "1":
            voti.mostra_dati()
        elif scelta == "2":
            voti.aggiungi_voto(materia=input(f"{Fore.CYAN}Inserisci la materia: {Style.RESET_ALL}"),
            voto=int(input(f"{Fore.CYAN}Inserisci il voto: {Style.RESET_ALL}")))
        elif scelta == "3":
            voti.rimuovi_voto(materia=input(f"{Fore.CYAN}Inserisci la materia: {Style.RESET_ALL}"),
                               voto=int(input(f"{Fore.CYAN}Inserisci il voto da rimuovere: {Style.RESET_ALL}")))
        elif scelta == "4":
            assenze.mostra_dati()
        elif scelta == "5":
            nuove_assenze = input(f"{Fore.CYAN}Inserisci le nuove assenze separate da virgola: {Style.RESET_ALL}")
            assenze.aggiungi_assenze([a.strip() for a in nuove_assenze.split(",")])
            print(f"{Fore.GREEN}Assenze aggiunte con successo!{Style.RESET_ALL}")
        elif scelta == "6":
            print(f"{Fore.GREEN}Grazie per aver usato il programma!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Scelta non valida. Riprova.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
