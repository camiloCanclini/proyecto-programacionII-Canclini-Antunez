from core import app
from flask import render_template, request
from core.functions import *

@app.route("/holaservicio")
def respuesta():
    return "<h1>Holaa chee</h1>"