## 2. lekce Python, Czechitas, Podzim 2023

pekarna = {
    "houska": 10,
    "rohlik": 2,
    "chleba": 40,
    "loupak": 20    
}

print(pekarna)
print(pekarna["houska"])
klic = "rohlik"
print(f"klic: {klic}, hodnota: {pekarna[klic]}")

##
produkt = input("Zadej produkt: ")
## osetrit chyby, viz nize
# print(f"{produkt} stojí {pekarna[produkt]} korun.")

## kontrola mame/nemame klic ve slovniku

if produkt in pekarna: # produkt je v pekarne = klic je ve slovniku
    print(f"{produkt} stojí {pekarna[produkt]} korun.")
else: # produkt neni v pekarne = klic není ve slovniku
    print(f"Bohužel, produkt {produkt} neprodáváme.")