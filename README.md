# Lab Reserve - A Flask-based Scheduler for Laboratory Researchers


## Why Lab Reserve? 

I am in a small biomedical research lab with many experimental equiptment that we have to share with each other. Currently we are using a web-based scheduler but its UI/UX is really frustrating. So I made a reservation scheduler with modern UI that will enable you to reserve anything equiptment you want to use within 5s! 


## What is Lab Reserve? 

See our demo video! 
https://youtu.be/iKAdm-ZGjIc

The calendar is enabled by FullCalendar Library. 


## Setting up this application in your environment

### activate venv environment
```
. venv/bin/activate
```

### setup
```
export FLASK_ENV=development
export FLASK_APP=flaskr
```

### install packages
```
pip install flask
```

## project layout
```
/flask-calendar
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── calendar.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── calendar/
│   │       └── cal.html
│   └── static/
│       ├── style.css
|       └── fullcalendar/ 
|           ├── main.css
|           └── main.js
├── venv/
├── .gitignore
├── package-lock.json
└── README.md
```
