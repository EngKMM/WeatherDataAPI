import flask
from flask import render_template
import pandas as pd

app=flask.Flask(__name__)

stations = pd.read_csv("data/stations.txt", skiprows=17)

@app.route("/")
def home():
    return render_template("Home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def call(station, date):
    file = ("data/TG_STAID" + str(station).zfill(6) + ".txt")
    df = pd.read_csv(file, skiprows= 20, parse_dates=['    DATE'])
    temp = df.loc[df['    DATE'] == date]['   TG'].squeeze() /10
    return {
        "temperature":temp,
        "date": date,
        "station": station
    }

@app.route("/api/v1/<station>")
def station_report(station):
    file = ("data/TG_STAID" + str(station).zfill(6) + ".txt")
    station = pd.read_csv(file, skiprows=20, parse_dates=['    DATE'])
    results = station.to_dict(orient = "records")
    return results

@app.route("/api/v1/year/<station>/<year>")
def yearly_report(station, year):
    file = ("data/TG_STAID" + str(station).zfill(6) + ".txt")
    df = pd.read_csv(file, skiprows=20, parse_dates=['    DATE'])
    results = df.loc[df['    DATE'].dt.year == int(year)]
    return results.to_dict(orient = "records")

@app.route("/api/v1/<station>/<date>")
def call(station, date):
    file = ("data/TG_STAID" + str(station).zfill(6) + ".txt")
    df = pd.read_csv(file, skiprows= 20, parse_dates=['    DATE'])
    temp = df.loc[df['    DATE'] == date]['   TG'].squeeze() /10
    return {
        "temperature":temp,
        "date": date,
        "station": station
    }

if __name__ == "__main__":
    app.run(debug=True)
