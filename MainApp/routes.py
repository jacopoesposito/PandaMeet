from flask import Blueprint, render_template, redirect, url_for, flash
from __init__ import login_required
from models import Users

mainapp = Blueprint('MainApp', __name__)



@mainapp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template("index.html")