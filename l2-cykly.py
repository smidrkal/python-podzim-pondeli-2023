sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

for kniha in sales:
    print(f"Kniha s názvem {kniha} se prodalo {sales[kniha]} ks.")

## a stejně pokud klíč je číslo a hodnota řetězec (ref. tombola v l2-cv3.py)

# jake jsou klice ve slovniku?
print(sales.keys())

# jake jsou hodnoty ve slovniku?
print(sales.values())

# kolik se prumerne prodalo vytisku na knihu?
print(sum(sales.values())/len(sales))

for nazev, prodano in sales.items():
    print(f"Kniha s názvem {nazev} se prodalo {prodano} ks.")