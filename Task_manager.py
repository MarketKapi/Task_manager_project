# Seznam pro ukládání úkolů
ukoly = []

def hlavni_menu():
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba. Zadejte číslo mezi 1 a 4.")

def pridat_ukol():
    while True:
        nazev = input("\nZadejte název úkolu: ").strip()
        if not nazev:
            print("Název úkolu nesmí být prázdný. Zkuste to, prosím, znovu.")
            continue

        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný. Zkuste to, prosím, znovu.")
            continue

        ukol = {"nazev": nazev, "popis": popis}
        ukoly.append(ukol)
        print(f"Úkol ‘{nazev}’ byl přidán.")
        break

def zobrazit_ukoly():
    if not ukoly:
        print("\nNemáte žádný uložený úkol.")
        return

    print("\nSeznam uložených úkolů:")
    for idx, ukol in enumerate(ukoly, start=1):
        print(f"{idx}. {ukol['nazev']} - {ukol['popis']}")

def odstranit_ukol():
    if not ukoly:
        print("\nNic k odstranění, seznam úkolů je prázdný.")
        return

    print("\nSeznam úkolů:")
    for idx, ukol in enumerate(ukoly, start=1):
        print(f"{idx}. {ukol['nazev']} - {ukol['popis']}")

    while True:
        volba = input("Zadejte číslo úkolu, který chcete odstranit: ").strip()
        
        if not volba.isdigit():
            print("Neplatný vstup. Zadejte prosím číslo úkolu.")
            continue

        cislo = int(volba)

        if 1 <= cislo <= len(ukoly):
            odebrany = ukoly.pop(cislo - 1)
            print(f"Úkol „{odebrany['nazev']}“ byl odstraněn.")
            break
        else:
            print(f"Úkol číslo {cislo} neexistuje. Zadejte číslo od 1 do {len(ukoly)}.")

# Spuštění programu
if __name__ == "__main__":
    hlavni_menu()