

from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config['MONGO_DBNAME']='toydb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/toydb'

mongo = PyMongo(app)
"""
1.  Programming languages: Python, HTML, JavaScript
2.  Web Development Application Framework: Flask
3.  Build tool: pip/virtualenv
4.  Static analysis bug finder tool: pylint
5.  Unit testing tool: pytest
6.  Persistent Data Source: MySQL
7.  Continuous integration tool: Travis-CI
"""

@app.route("/")
@app.route("/index")
def index():
    stocks = mongo.db.stocks # create a collection called stocks
    output = [stock["ticker"] for stock in stocks.find()]
    return render_template("index.html", stocks=output)

@app.route("/add_stock", methods=["POST"])
def add_stock():
    print(request.form["ticker"])
    stocks = mongo.db.stocks # create a collection called stocks
    ticker = request.form["ticker"]
    ticker_id = stocks.insert({"ticker": ticker})

    output = [stock["ticker"] for stock in stocks.find()]
    return ",".join(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
