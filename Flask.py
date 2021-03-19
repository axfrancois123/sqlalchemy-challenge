
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///titanic.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.stations
Measurement = Base.classes.measurement

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start> and /api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
     precipitation_scores = session.query(Measurement.date, func.avg(Measurement.prcp)).\
                    filter(Measurement.date >= year_ago).\
                    group_by(Measurement.date).all()
     prcp_nums = []
    for result in precipitation_scores:
        row = {}
        row["date"] = result[0]
        row["prcp"] = result[1]
        prcp_nums.append(row)
   
    return jsonify(prcp_nums)

@app.route("/api/v1.0/stations")
def station():
    stations = session.query(Station).all()
    return jsonify(stations.to_dict())


if __name__ == '__main__':
    app.run(debug=True)
