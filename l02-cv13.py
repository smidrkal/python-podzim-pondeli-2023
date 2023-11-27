## https://kodim.cz/programovani/uvod-do-progr-2/uvod-do-programovani-2/slovniky/slovniky/tombola

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

cislo_listku = input("Zadej číslo lístku: ")
cislo_listku = int(cislo_listku)
#print(cislo_listku+1)

if cislo_listku in tombola:
    print(f"Lístek {cislo_listku} vyhrává: {tombola[cislo_listku]}.") 
else:
    print(f"Bohužel, lístek {cislo_listku} nic nevyhrává.")