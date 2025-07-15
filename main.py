import flask
from flask import render_template
import pandas as pd

app=flask.Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html")

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
