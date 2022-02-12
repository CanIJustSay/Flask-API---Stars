from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

df = pd.read_csv("complete.csv")

data = [
    {
        "radius": df["Radius"].tolist()
    },
    {
        "mass": df["Mass"].tolist()
    },
    {
        "gravity": df["Gravity"].tolist()
    },
    {
        "distance": df["Distance"].tolist()
    },
    {
        "starname": df["Star name"].tolist()
    }
]

@app.route('/getData')
def fetchData():
    return jsonify(({
        "data": data
    }))


if(__name__ == '__main__'):
    app.run(debug=True)