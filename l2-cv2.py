## https://kodim.cz/programovani/uvod-do-progr-2/uvod-do-programovani-2/slovniky/slovniky/detektivky

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales["Noc, která mě zabila"] = 0
#sales["Vrah zavolá v deset"] = sales["Vrah zavolá v deset"]+100 # taky jde, ale fakt zbytečné...
sales["Vrah zavolá v deset"] += 100

print(sales)