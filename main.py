
from weerstation import weerstation
from smart_controller import smart_app_controller
from weer_api import haal_temperatuur_op


def hoofdmenu():
    while True:

        print("\n===== SMART APP PLATFORM =====")
        print("1. Weerstation")
        print("2. Smart App Controller")
        print("3. Actuele temperatuur Utrecht")
        print("4. Stoppen")

        try:
            keuze = int(input("Maak een keuze: "))

        except ValueError:
            print("Voer een getal in.")
            continue

        if keuze == 1:
            weerstation()á

        elif keuze == 2:
            smart_app_controller()

        elif keuze == 3:
            haal_temperatuur_op()

        elif keuze == 4:
            print("Smart App Platform afgesloten.")
            break

        else:
            print("Ongeldige keuze. Probeer opnieuw.")


if __name__ == "__main__":
    hoofdmenu()

