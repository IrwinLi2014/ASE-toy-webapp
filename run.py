
import pymongo
from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

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
def hello():
    return render_template("index.html")

@app.route("/add_stock", methods=["POST"])
def add_stock(data):
	# TODO: add pymongo stuff
	return "SUCCESS"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)