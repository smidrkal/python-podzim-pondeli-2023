# https://kodim.cz/programovani/uvod-do-progr-2/uvod-do-programovani-2/slovniky/excs/ctenar

books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

# spocti celkovy pocet prectenych stran
stran=0
for kniha in books:
    stran += kniha["pages"]
print(f"Celkem bylo přečteno {stran} stran.")

print("Knihy s hodnocením alespoň 8:")
for kniha in books:
    if kniha["rating"] >= 8:
        print(kniha["title"])