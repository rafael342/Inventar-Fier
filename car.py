import datetime

def adauga_material(material, cantitate, inventar):
    try:
        cantitate = float(cantitate)
    except ValueError:
        print("Cantitatea introdusă nu este validă.")
    else:
        ora_adaugare = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if material in inventar:
            inventar[material].append((ora_adaugare, cantitate))
        else:
            inventar[material] = [(ora_adaugare, cantitate)]
        print(f"{cantitate} unități de {material} au fost adăugate cu succes în inventar.")

def afiseaza_inventar(inventar):
    for material, adaugari in inventar.items():
        print(f"{material}:")
        for adaugare in adaugari:
            ora_adaugare, cantitate = adaugare
            print(f"   {ora_adaugare} - Cantitate: {cantitate}")

def main():
    inventar = {}
    while True:
        print("\n1. Adaugă fier")
        print("2. Adaugă tablă")
        print("3. Adaugă aluminiu")
        print("4. Adaugă cupru")
        print("5. Afisează inventar")
        print("6. Ieșire")

        optiune = input("Alege o opțiune: ")

        if optiune == "1":
            cantitate = input("Introdu cantitatea de fier adăugată: ")
            adauga_material("fier", cantitate, inventar)
        elif optiune == "2":
            cantitate = input("Introdu cantitatea de tablă adăugată: ")
            adauga_material("tablă", cantitate, inventar)
        elif optiune == "3":
            cantitate = input("Introdu cantitatea de aluminiu adăugată: ")
            adauga_material("aluminiu", cantitate, inventar)
        elif optiune == "4":
            cantitate = input("Introdu cantitatea de cupru adăugată: ")
            adauga_material("cupru", cantitate, inventar)
        elif optiune == "5":
            afiseaza_inventar(inventar)
        elif optiune == "6":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă! Te rog să alegi din nou.")

if __name__ == "__main__":
    main()





















































