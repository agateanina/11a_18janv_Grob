import csv
datnes_nosaukums=input("Ievadi datnes nosaukumu:")

try:
    with open(datnes_nosaukums, newline='', encoding='utf8') as csvfile:
        csvlasitajs=csv.reader(csvfile)
        for rinda in csvlasitajs:
            print(rinda)
except FileNotFoundError:
    print(f"datnes ar nosaukumu{datnes_nosaukums} nav atrasta.")
except StopIteration:
    print("datne ir tukša.")
except Exception as e:
    print(f"Notikusi kļūda: {e}")
