def lasit_datni():
    datnes_nosaukums=input("ievadīt datnes nosaukumu:")

    try:
        with open(datnes_nosaukums, 'r') as skaitli:
            saturs=skaitli.read()

    except FileNotFoundError:
            print("datne nav atrasta.")

            print(saturs)
