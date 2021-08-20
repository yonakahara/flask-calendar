import functools
import re
import json
import collections

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, request, jsonify, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('calendar', __name__, url_prefix='/cal')

@bp.route("/", methods=("GET", "POST"))
def show_cal():
    db = get_db()
    if request.method == "POST": 
        current_app.logger.debug(request.form)
        date_start = request.form['date_start']
        date_end = request.form['date_end']
        event_title = request.form['event_title']

        # store event to database
        db.execute("INSERT INTO event (user_id, start, end, title) VALUES (?, ?, ?, ?)", 
                   (1, date_start, date_end, event_title))
        db.commit()

        # ajax
        if date_start and date_end and event_title:
            return jsonify({'start':date_start, 'end':date_end, 'title':event_title})
        return jsonify({'error' : 'Missing data!'})
    
    # GET: take out events and pass to calendar object
    events_rows = db.execute("SELECT * FROM event WHERE user_id = 1").fetchall()
    events_list = []
    for row in events_rows: 
        d = collections.OrderedDict()
        d["start"] = row["start"]
        d["end"] = row["end"]
        d["title"] = row["title"]
        # d["user_id"] = int(row["user_id"])
        events_list.append(d)
    return render_template("calendar/cal.html", events = events_list)