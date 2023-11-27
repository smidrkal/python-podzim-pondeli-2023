# https://kodim.cz/programovani/uvod-do-progr-2/uvod-do-programovani-2/slovniky/excs

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

#print(sum(sales.values())/len(sales))
prum_znamka = sum(school_report.values())/len(school_report)
print(f"Průměrná známka ze všech předmětů je {prum_znamka}.")

print("Jedničku získal žák z následujících předmětů:")
for predmet, znamka in school_report.items():
    if znamka == 1:
        print(predmet)
