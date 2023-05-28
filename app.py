from flask import Flask, render_template
from utils import load_hotels, get_departure, get_city

app = Flask(__name__)


class Hotel:
    def __init__(self, id, title, description, picture):
        self.id = id
        self.title = title
        self.description = description
        self.picture = picture

    def __repr__(self):
        return '<Hotel %r>' % self.id


@app.route("/")
def index():
    hotels = load_hotels()
    tours = [Hotel(key, hotel["title"], hotel["description"], hotel["picture"]) for key, hotel in hotels.items()]
    return render_template("index.html", tours=tours)


@app.route("/tour/<int:id>")
def tour(id):
    tour = load_hotels()[str(id)]
    stars = int(tour["stars"]) * "★"
    departure = get_departure(tour["departure"])
    return render_template("tour.html", tour=tour, stars=stars, departure=departure)


@app.route("/<string:departure>")
def msk_tours(departure):
    sort_tours = get_city(departure)
    tours = [Hotel(key, hotel["title"], hotel["description"], hotel["picture"]) for key, hotel in sort_tours.items()]
    return render_template("index.html", tours=tours)


if __name__ == "__main__":
    app.run(debug=True)
