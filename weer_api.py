
import urllib.request
import urllib.error
import json


def haal_temperatuur_op():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=52.09&longitude=5.12"
        "&current=temperature_2m"
        "&timezone=Europe%2FAmsterdam"
    )

    try:
        with urllib.request.urlopen(url, timeout=10) as antwoord:
            gegevens = json.loads(
                antwoord.read().decode("utf-8")
            )

        temperatuur = gegevens["current"]["temperature_2m"]

        print(
            "Actuele temperatuur in Utrecht:",
            temperatuur,
            "°C"
        )

    except urllib.error.URLError:
        print("Kan geen verbinding maken met de weer API.")

    except (json.JSONDecodeError, KeyError, TypeError):
        print("De ontvangen weergegevens zijn ongeldig.")

    except TimeoutError:
        print("De aanvraag duurde te lang.")


if __name__ == "__main__":
    haal_temperatuur_op()

