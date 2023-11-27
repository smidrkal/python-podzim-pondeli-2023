# https://kodim.cz/programovani/uvod-do-progr-2/uvod-do-programovani-2/slovniky/excs/spz

plates = {"4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"
}

for znacka, majitel in plates.items():
    if znacka[1] == "P":
        print(f"Majitelem plzenske SPZ {znacka} je {majitel}.")