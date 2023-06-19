
# absoluter Pfad:
file_path = r"C:\FIAE\programme\log_data.txt"

# relativer Pfad:
#file_path = r"Desktop\log_data.txt"

"""Frage:
Welche und wieviele IPs wurden pro Jahr geloggt?

{
    "2022": ["254.32.180.106", ...]
    "2023": ["55.206.12.34", ...]
}
"""

"""Frage:
Welche und wieviele IPs wurden pro Jahr und Monat geloggt?

{
    "2022": {
        "01": ["254.32.180.106", ...],
        "02": ["...", ..."],
        ...
    },
    "2023": {
        "01": ["254.32.180.106", ...],
        "02": ["...", ..."],
        ...
    }
}
"""

ip_by_year = {}

with open(file_path, encoding="utf-8") as file:
    #print(file.read())
    #print(file.readlines())
    for line in file:
        line = line.split(",")
        date = line[0]
        ip = line[1].strip()
        # 1) Jahr extrahieren
        year = date.split(".")[2]
        month = date.split(".")[1]
        
        # 2) dict aufbauen bzw. verändern
        ip_by_year.setdefault(year, {})
        ip_by_year[year].setdefault(month,[])
        
        # 3) ip adresse passend einfügen
        ip_by_year[year][month].append(ip)
        #print(ip_by_year)
        
        #print()
        
print("IPs pro Jahr:")

for year,all_month in sorted(ip_by_year.items()):
    print(year)
    for month,value in sorted(all_month.items()):
        print("Monat:",month)
        print("Anzahl IPs:", len(value))
        print()

#print(ip_by_year)
