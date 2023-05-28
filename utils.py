import json


def load_hotels():
    with open("tour.json", encoding="utf-8") as file:
        hotels = json.loads(file.read())
        return hotels


def get_departure(departure):
    if departure == "ekb":
        return "Екатеринбурга"
    elif departure == "nsk":
        return "Новосибирска"
    elif departure == "msk":
        return "Москвы"
    elif departure == "spb":
        return "Санкт_Петербурга"
    elif departure == "kazan":
        return "Казани"


def get_city(departure):
    hotels = load_hotels()
    tours_sort = {key: value for key, value in hotels.items() if value["departure"] == departure}
    return tours_sort
