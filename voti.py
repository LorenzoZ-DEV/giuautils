from colorama import Fore, Style
from tabulate import tabulate

class Voti:
    def __init__(self):
        self.voti = {
            "Gestione Progetto": [3],
            "Italiano": [],
            "Storia": [],
            "Informatica": [],
            "Matematica": [],
            "Inglese": [],
            "Sistemi e Reti": [],
            "TPST": [],
        }

    def calcola_medie(self):
        medie = {}
        for materia, voti in self.voti.items():
            if voti:
                medie[materia] = sum(voti) / len(voti)
            else:
                medie[materia] = None
        return medie

    def materie_sotto_sufficienza(self):
        materie_insufficienti = []
        for materia, voti in self.voti.items():
            if voti and (sum(voti) / len(voti)) < 6:
                materie_insufficienti.append(materia)
        return materie_insufficienti


    def aggiungi_voto(self, materia, voto):
        if materia in self.voti:
            self.voti[materia].append(voto)
            print(f"{Fore.GREEN}Voto aggiunto con successo!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Materia non trovata!{Style.RESET_ALL}")

    def rimuovi_voto(self, materia, voto):
        if materia in self.voti:
            if voto in self.voti[materia]:
                self.voti[materia].remove(voto)
                print(f"{Fore.GREEN}Voto rimosso con successo!{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Voto non trovato!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Materia non trovata!{Style.RESET_ALL}")

    def mostra_dati(self):
        materie_insufficienti = self.materie_sotto_sufficienza()

        print("\nMaterie sotto la sufficienza:")
        if materie_insufficienti:
            for materia in materie_insufficienti:
                print(f"{Fore.RED}{materia}{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Nessuna materia sotto la sufficienza!{Style.RESET_ALL}")

        print("\nTabella delle medie:")
        table = []
        for materia, voti in self.voti.items():
            if voti:
                media = sum(voti) / len(voti)
                stato = f"{Fore.GREEN}Sufficiente{Style.RESET_ALL}" if media >= 6 else f"{Fore.RED}Insufficiente{Style.RESET_ALL}"
                table.append([materia, f"{media:.2f}", stato])
            else:
                table.append([materia, "Nessuna Valutazione", "N/A"])
        print(tabulate(table, headers=["Materia", "Media", "Stato"], tablefmt="grid"))

# Example usage
voti = Voti()
voti.mostra_dati()
