import functools
import re

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, request, jsonify, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('calendar', __name__, url_prefix='/cal')

@bp.route("/", methods=("GET", "POST"))
def show_cal():
    current_app.logger.debug(request.method)
    if request.method == "POST": 
        current_app.logger.debug(request.form)
        date_start = request.form['date_start']
        date_end = request.form['date_end']
        event_title = request.form['event_title']
        output = "event {} is from {} to {}. ".format(event_title, date_start, date_end)
        current_app.logger.debug(output)
        if date_start and date_end and event_title:
            return jsonify({'start':date_start, 'end':date_end, 'title':event_title})
        return jsonify({'error' : 'Missing data!'})
    return render_template("calendar/cal.html")