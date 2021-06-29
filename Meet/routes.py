from flask import Blueprint, render_template, redirect, url_for, flash
from __init__ import login_required


meet = Blueprint('Meet', __name__)

@meet.route('/meet', methods=['GET', 'POST'])
@login_required

def meetInit():
    return render_template('meet.html')