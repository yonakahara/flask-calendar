import functools
import re
import json
import collections

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, request, jsonify, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db
from flaskr.auth import login_required

bp = Blueprint('calendar', __name__, url_prefix='/cal')

@bp.route("/", methods=("GET", "POST"))
@login_required
def show_cal():
    db = get_db()
    if request.method == "POST": 
        current_app.logger.debug(request.form)
        date_start = request.form['date_start']
        date_end = request.form['date_end']
        event_title = request.form['event_title']

        # store event to database
        db.execute("INSERT INTO event (user_id, start, end, title) VALUES (?, ?, ?, ?)", 
                   (session['user_id'], date_start, date_end, event_title))
        db.commit()

        # ajax
        if date_start and date_end and event_title:
            return jsonify({'start':date_start, 'end':date_end, 'title':event_title})
        return jsonify({'error' : 'Missing data!'})
    
    # GET: take out events and pass to calendar object
    # current_app.logger.debug(session["user_id"])
    events_rows = db.execute("SELECT * FROM event WHERE user_id = ?", (session["user_id"],)).fetchall()
    events_list = []
    for row in events_rows: 
        d = collections.OrderedDict()
        d["id"] = row["id"]
        d["start"] = row["start"]
        d["end"] = row["end"]
        d["title"] = row["title"]
        d["classNames"] = "id-" + str(row["id"])
        events_list.append(d)
    # current_app.logger.debug(events_list)
    return render_template("calendar/cal.html", events = events_list)

# update event
@bp.route("/update", methods=("GET", "POST")) # methods=を消すとなぜかバグる(403)
def update_event(): 
    r = request.form
    # update event object
    db = get_db()
    db.execute("UPDATE event SET (start, end, title) = (?, ?, ?) WHERE user_id = ? AND start like ? AND title = ?", 
               (r["event[start]"], r["event[end]"], r["event[title]"], session["user_id"], 
                r["event_old[start]"], r["event_old[title]"]))
    db.commit()
    return redirect(url_for("calendar.show_cal"))

# delete event
@bp.route("/delete", methods=("GET", "POST")) # methods=を消すとなぜかバグる(403)
def delete_event(): 
    r = request.form
    # delete event from db
    db = get_db()
    db.execute("DELETE FROM event WHERE id = ? AND user_id = ?", 
               (request.form["id"], session["user_id"]))
    db.commit()
    return redirect(url_for("calendar.show_cal"))