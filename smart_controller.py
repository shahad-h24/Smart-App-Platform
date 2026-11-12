
def aantal_dagen(inputFile):
    try:
        with open(inputFile, "r") as bestand:
            regels = bestand.readlines()

        return max(0, len(regels) - 1)

    except FileNotFoundError:
        print("Het invoerbestand is niet gevonden.")
        return 0


def auto_bereken(inputFile, outputFile):
    try:
        with open(inputFile, "r") as bestand:
            regels = bestand.readlines()

        resultaten = []

        for regel in regels[1:]:
            if regel.strip() == "":
                continue

            gegevens = regel.replace(";", " ").split()

            if len(gegevens) < 5:
                print("Ongeldige informatie in het invoerbestand.")
                continue

            datum = gegevens[0]
            aantal_personen = int(gegevens[1])
            temperatuur_ingesteld = float(gegevens[2])
            temperatuur_buiten = float(gegevens[3])
            neerslag = float(gegevens[4])
á
            verschil = temperatuur_ingesteld - temperatuur_buiten

            if verschil >= 20:
                cv = 100
            elif verschil >= 10:
                cv = 50
            else:
                cv = 0

            ventilatie = min(aantal_personen + 1, 4)

            if neerslag < 3:
                bewatering = True
            else:
                bewatering = False

            resultaten.append(
                f"{datum};{cv};{ventilatie};{bewatering}"
            )

        with open(outputFile, "w") as bestand:
            for resultaat in resultaten:
                bestand.write(resultaat + "\n")

        print("De automatische berekening is klaar.")

    except FileNotFoundError:
        print("Het invoerbestand is niet gevonden.")

    except (ValueError, IndexError):
        print("Er staat ongeldige informatie in het invoerbestand.")

    except OSError:
        print("Er is een fout met het bestand opgetreden.")


def overwrite_settings(outputFile):
    try:
        datum = input("Welke datum wil je aanpassen? ")

        print("1. CV")
        print("2. Ventilatie")
        print("3. Bewatering")

        systeem = int(input("Welk systeem wil je aanpassen? "))

        if systeem not in [1, 2, 3]:
            return -3

        waarde = input("Welke nieuwe waarde wil je instellen? ")

        with open(outputFile, "r") as bestand:
            regels = bestand.readlines()

        datum_gevonden = False
        nieuwe_regels = []

        for regel in regels:
            gegevens = regel.strip().split(";")

            if len(gegevens) != 4:
                nieuwe_regels.append(regel)
                continue

            if gegevens[0] == datum:
                datum_gevonden = True

                if systeem == 1:
                    nieuwe_waarde = int(waarde)

                    if not 0 <= nieuwe_waarde <= 100:
                        return -3

                    gegevens[1] = str(nieuwe_waarde)

                elif systeem == 2:
                    nieuwe_waarde = int(waarde)

                    if not 0 <= nieuwe_waarde <= 4:
                        return -3

                    gegevens[2] = str(nieuwe_waarde)

                elif systeem == 3:
                    if waarde == "0":
                        gegevens[3] = "False"
                    elif waarde == "1":
                        gegevens[3] = "True"
                    else:
                        return -3

                nieuwe_regels.append(";".join(gegevens) + "\n")

            else:
                nieuwe_regels.append(regel)

        if not datum_gevonden:
            return -1

        with open(outputFile, "w") as bestand:
            bestand.writelines(nieuwe_regels)

        return 0

    except FileNotFoundError:
        print("Het uitvoerbestand is niet gevonden.")
        return -3

    except (ValueError, IndexError):
        return -3

    except OSError:
        print("Er is een fout met het bestand opgetreden.")
        return -3


def smart_app_controller():
    inputFile = "input.txt"
    outputFile = "output.txt"

    while True:
        print("\nSMART APP CONTROLLER")
        print("1. Aantal dagen")
        print("2. Automatisch berekenen")
        print("3. Instellingen aanpassen")
        print("4. Stoppen")

        try:
            keuze = int(input("Maak een keuze: "))

        except ValueError:
            print("Voer een getal in.")
            continue

        if keuze == 1:
            print("Aantal dagen:", aantal_dagen(inputFile))

        elif keuze == 2:
            auto_bereken(inputFile, outputFile)

        elif keuze == 3:
            resultaat = overwrite_settings(outputFile)

            if resultaat == 0:
                print("Instellingen zijn aangepast.")

            elif resultaat == -1:
                print("Deze datum is niet gevonden.")

            elif resultaat == -3:
                print("Ongeldig systeem of ongeldige waarde.")

        elif keuze == 4:
            print("Smart App Controller afgesloten.")
            break

        else:
            print("Ongeldige keuze. Probeer opnieuw.")


if __name__ == "__main__":
    smart_app_controller()

