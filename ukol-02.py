sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

'''
Napiš software, který bude využívat prodavač v případě, že do obchodu přijde zákazník.
Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. 
Obě informace si ulož. Následně naprogramuj následující varianty:

Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš tedy zprávu, že součástka není skladem.
Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník,
    vypiš text o tom, že lze prodat pouze omezené množství kusů. 
    Následně součástku odeber ze slovníku, protože je vyprodaná.
Pokud zadaná součástka na skladě je a je jí dostatek,
    vypiš informaci, že poptávku lze uspokojit v plné výši, 
    a sniž počet součástek na skladě o množství požadované zákazníkem.
'''

soucastka = input("Zadej kód součástky: ")
mnozstvi = int(input("Zadej množství: "))

if soucastka not in sklad:
    print(f"Součástka {soucastka} není skladem.")
else:
    if sklad[soucastka] < mnozstvi:
        print(f"Součástky {soucastka} není dostatečné množství skladem. Je možné vydat jen {sklad[soucastka]} ks.")
        sklad.pop(soucastka)
    else:
        print(f"Součástky lze dodat v požadovaném množství.")
        sklad[soucastka] -= mnozstvi 