from datetime import datetime, timedelta
from colorama import Fore, Style

class Assenze:
    def __init__(self):
        self.assenze = []

    def aggiungi_assenze(self, assenze):
        self.assenze.extend(assenze)

    def analizza_assenze(self):
        ritardi = [a for a in self.assenze if "Ritardo" in a]
        uscite_anticipate = [a for a in self.assenze if "Uscita anticipata" in a]
        assenze_complete = [a for a in self.assenze if "Assenza" in a]
        return ritardi, uscite_anticipate, assenze_complete

    def mostra_ascii(self):
        ascii_art = f"""
{Fore.RED} █████╗ ███████╗███████╗███████╗███╗   ██╗███████╗███████╗
{Fore.RED}██╔══██╗██╔════╝██╔════╝██╔════╝████╗  ██║╚══███╔╝██╔════╝
{Fore.RED}███████║███████╗███████╗█████╗  ██╔██╗ ██║  ███╔╝ █████╗  
{Fore.RED}██╔══██║╚════██║╚════██║██╔══╝  ██║╚██╗██║ ███╔╝  ██╔══╝  
{Fore.RED}██║  ██║███████║███████║███████╗██║ ╚████║███████╗███████╗
{Fore.RED}╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝
                                                          
{Style.RESET_ALL}
"""
        print(ascii_art)

    def mostra_dati(self):
        self.mostra_ascii()  # Mostra l'ASCII art prima dei dati
        ritardi, uscite_anticipate, assenze_complete = self.analizza_assenze()

        print(f"\n{Fore.YELLOW}Ritardi: {len(ritardi)}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Uscite anticipate: {len(uscite_anticipate)}{Style.RESET_ALL}")
        print(f"{Fore.RED}Assenze complete: {len(assenze_complete)}{Style.RESET_ALL}")
