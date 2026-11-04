
def fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - luchtvochtigheid / 100 * windsnelheid


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(
        temp_celcius, windsnelheid, luchtvochtigheid
    )

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"

    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"

    elif 0 <= gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"

    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"

    elif 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."

    else:
        return "Warm! Airco aan!"


def invoer_getal(vraag, minimum=None, maximum=None):
    while True:
        try:
            waarde = float(input(vraag))

            if minimum is not None and waarde < minimum:
                print("Waarde te laag. Probeer opnieuw.")
                continue

            if maximum is not None and waarde > maximum:
                print("Waarde te hoog. Probeer opnieuw.")
                continue

            return waarde

        except ValueError:
            print("Ongeldige invoer. Probeer opnieuw.")


def gegevens_opslaan(temp, windsnelheid, luchtvochtigheid, rapport):
    try:
        with open("weerdata.txt", "a") as bestand:
            bestand.write(
                f"Temperatuur: {temp} C, "
                f"Windsnelheid: {windsnelheid} m/s, "
                f"Luchtvochtigheid: {luchtvochtigheid} %, "
                f"Rapport: {rapport}\n"
            )

    except OSError:
        print("Fout bij het opslaan van de gegevens.")


def weerstation():
    totaal_temp = 0
    aantal_dagen = 0

    for dag in range(1, 8):
        print(f"\n--- Dag {dag} ---")

        while True:
            invoer_temp = input(
                "Wat is de temperatuur [C]? "
                "(Druk op Enter om te stoppen): "
            )

            if invoer_temp == "":
                print("Weerstation afgesloten.")
                return

            try:
                temp = float(invoer_temp)

                if temp < -50 or temp > 60:
                    print("Ongeldige temperatuur. Probeer opnieuw.")
                    continue

                break

            except ValueError:
                print("Ongeldige invoer. Probeer opnieuw.")

        windsnelheid = invoer_getal(
            "Wat is de windsnelheid [m/s]? ", 0
        )

        luchtvochtigheid = invoer_getal(
            "Wat is de luchtvochtigheid [%]? ", 0, 100
        )

        temp_f = fahrenheit(temp)

        rapport = weerrapport(
            temp, windsnelheid, luchtvochtigheid
        )

        totaal_temp += temp
        aantal_dagen += 1

        gemiddelde = totaal_temp / aantal_dagen

        print(f"\nTemperatuur: {temp:.1f} C ({temp_f:.1f} F)")
        print(rapport)
        print(f"Gemiddelde temperatuur: {gemiddelde:.1f} C")

        gegevens_opslaan(
            temp, windsnelheid, luchtvochtigheid, rapport
        )

        print("======================================")


if __name__ == "__main__":
    weerstation()

