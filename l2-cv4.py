## https://kodim.cz/programovani/uvod-do-progr-2/uvod-do-programovani-2/slovniky/slovniky/vecirek

passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

uzivatel = input("Zadej uživatele: ")
from getpass import getpass
heslo = getpass("Zadej heslo: ")
print("========")
if uzivatel in passwords:
    #heslo_ulozene = passwords[uzivatel]
    if heslo == passwords[uzivatel]:
        print(">> Smíš vstoupit.")
    else:
        # tohle je jen pro účely učení, bezpečnostní pravidlo je dát stejnou hlášku jako v případě ne-existujícího uživatele
        print(">> Špatné heslo")
else:
    print(">> Neznámý uživatel")