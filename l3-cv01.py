import json
with open('l3-zavod.json', encoding='utf-8') as file:
    runners = json.load(file)

winner = runners[0]
winner_time = winner["casy"]["oficialni"]

####
'''

1
Závod
Pracuj dál se souborem zavod.json a zjisti čas závodníka, který získal stříbrnou medaili.
Dále projdi data pomocí cyklu a vytvoř seznam všech závodníků, kteří závod dokončili, tj. jejich oficiální čas není DNF.

Můžeš postupovat následujícím způsobem:

Vytvoř si prázdný seznam finishers, kam budeš vkládat jména závodníků, kteří závod doběhli.
* Pomocí cyklu projdi seznam závodníků. 
    Struktura vyjmuté položky bude obdobná jako struktura dat o vítězi závodu.
    Do cyklu vlož podmínku, která ověří, zda oficiální čas závodníka je odlišná od řetězce DNF.
* Dovnitř podmínky vlož kód, který vloží jméno závodníka do seznamu finishers.
* Na konec programu (mimo cyklus) vlož příkaz na vypsání obsahu seznamu finishers.
'''
print(f"vitez je {winner['jmeno']}")
print(f"cas ma {winner_time}")

finishers = []

for finisher in runners:
    if finisher["casy"]["oficialni"] != 'DNF':
        # print(f"zavodnik: {finisher['jmeno']} pridan do tabulky vitezu s casem {finisher['casy']['oficialni']}")
        finishers.append(finisher['jmeno'])
    #else:
    #    print(f"{finisher['jmeno']} nedokoncil")

print(f"{finishers}")