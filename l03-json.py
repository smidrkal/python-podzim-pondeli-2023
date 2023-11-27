# https://kodim.cz/programovani/uvod-do-progr-2/uvod-do-programovani-2/json/format-json
## popis json formatu a overovac validnosti kodu: https://jsonlint.com/
'''
priklad:
{
    "jmeno": "Petr",
    "prijmeni": "Roman",
    "rok": 2017,
    "dochazka": 0.95,
    "vyznamenani": true
}
'''
#######
import json 
## cteni
'''
with open('l3-absolventi.json', encoding='utf-8') as file:
    absolvents = json.load(file)
    ## python automaticky zavre soubor jakmile skonci dany blok
print(absolvents)
'''
## zapis
import json
hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
with open('l3-hodiny.json', mode='w', encoding='utf-8') as file:
    json.dump(hours, file, indent=4, ensure_ascii=False)
### funkce open
#### ofic. doc: https://docs.python.org/3/library/functions.html?highlight=open#open
#### jednodussi popis: https://www.programiz.com/python-programming/methods/built-in/open

### diakritika!
#### Funkce json.dump() ve výchozím nastavení překóduje non-ASCI znaky do jejich číselného kódu
#### Pokud chceš mít výstupní JSON v plném kódování UTF-8, lze toho dosáhnout volitelným parametrem `ensure_ascii=False`.

'''
#### 
'''
## oproti Python slovniku: uvozovky musi byt dvojite, true/false je vzdy malym pismenem (versus True/False u Pythonu)
## take do .json neni mozne pridavat komentare
#'''