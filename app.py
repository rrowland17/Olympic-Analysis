import os

import json
import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/olympicDataFinal.sqlite"

db = SQLAlchemy(app)

#engine = create_engine("sqlite:///olympicDataFinal.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
#print(Base.classes.keys())
Olympics = Base.classes.olympicdata

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/embed")
def embed():
    return render_template("embed.html")


@app.route("/analysis")
def analysis():
    return render_template("analysis.html")    

@app.route("/games")
def games():
    """Return a list of games."""

    #Query for the games
    
    results = db.session.query(Olympics.Games.distinct().label("Games"))
    games = [row.Games for row in results.all()]
    returngames=[]
    for x in games:
        if x != None:
            returngames.append(x)
    returngames.sort(reverse = True)
    
            

    #Return a list of the column names (games names)
    return jsonify(returngames)

@app.route("/medals/<games>")
def medals(games):

    results_2 = db.session.query(Olympics).filter(Olympics.Games==games)
    x = [row.Games for row in results_2.all()]
    y = [row.Medal for row in results_2.all()]
    z = [row.name for row in results_2.all()]
    lat = [row.latitude for row in results_2.all()]
    lon = [row.longitude for row in results_2.all()]

    rsdic={
            "Name": z, 
            "Medal":y, 
            "lat":lat, 
            "long":lon
            }
    pd_results=pd.DataFrame(rsdic)
    pd_results["Name"].value_counts()

    x=pd.DataFrame(pd_results.groupby(["Name", "Medal"]).count())
    del x['long']
    x = x.rename(columns={"lat":"count"})

    final = pd.merge(x, pd_results, how="left", on=["Name","Medal"])

    final.drop_duplicates().reset_index()
    final["gold"] = (final["Medal"]=="Gold")
    final["silver"] = final["Medal"]=="Silver"
    final["bronze"] = final["Medal"]=="Bronze"
    final["NM"] = final["Medal"]=="NM"
    final_g = final.groupby(["Name"]).agg({
    "lat": "max",
    "long": "max",
    "count": "max",
    "gold": "sum",
    "silver": "sum",
    "bronze": "sum",
    "NM": "sum"
    }) 
    return(final_g.reset_index().to_json(orient='records'))
@app.route("/map")
def show_map():
     return render_template('map.html')

if __name__ == "__main__":
    app.run(debug=True)