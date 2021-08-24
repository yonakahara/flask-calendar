# Lab Reserve - A Flask-based Scheduler for Laboratory Researchers


## Why Lab Reserve? 

I am in a small biomedical research lab with many experimental equipment that we have to share with each other. Currently we are using a web-based scheduler but its UI/UX is really frustrating. So I made a reservation scheduler with modern UI that will enable you to reserve any equipment you want to use within 5s! 


## What is Lab Reserve? 

See our demo video! 
https://youtu.be/iKAdm-ZGjIc

- Authorization: by registering your username and password, you can get your own calendar. 

- Calendar: you can make reservations by dropping blocks (equip. i & your username) onto your calendar. after creating event, you can change its duration or timing by drag & drop. by clicking on the delete button, you can delete the event. 

This application is using technologies such as Flask (python), JQuery. 

The calendar view is enabled by FullCalendar Library, a full-sized drag & drop JavaScript event calendar. 
https://fullcalendar.io/


## Setting up this application in your environment

### activate venv environment
using a virtual python environment will make your life easier:)
```
python3 -m venv venv
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
│   ├── __init__.py # initialize flask app
│   ├── db.py # database related configuration
│   ├── schema.sql # database schematics 
│   ├── auth.py # registration and login related 
│   ├── calendar.py # CRUD for calendar resources
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── calendar/
│   │       └── cal.html # js code and calendar view here 
│   └── static/
│       ├── style.css
|       └── fullcalendar/ # adapted from fullcalendar
|           ├── main.css
|           └── main.js
├── venv/ # virtual environment
├── .gitignore # define what files we don't need to commit
├── package-lock.json # js package manager
└── README.md
```

## discussion

My personal goal in this project is to master UI implementation using Javascript. During designing phase, I especially wanted to make calendar event creation experience just like what we have in iCalendar: drag wherever you want to create an event with any duration you want. But few sources explained enough on how to do this, and I was completely new to Javascript, so I had to give up and tried an easier one: drag and drop (which was friendly introduced in detail by FullCalendar). Next time, I would love to try different approaches to solve this puzzle. 

The CRUD model was implemented relatively smoothly using flask, but since the library we used to implement the calendar was JS, it was harder than expected. The CRUD model was implemented relatively smoothly using flask, but since the library we used to implement the calendar this time was JS, it was harder than expected to learn and implement JS and JQuery from scratch. However, thanks to this, I was able to learn technologies that greatly improve the webUI, such as asynchronous communication and DOM manipulation, and I am glad that I was able to actually implement relatively complex behavior using the library. In particular, I felt that the experience of reading the official documentation of the library and customizing it to the way I wanted to use it would be useful in the future. However, this time I chose flask as I was familiar with the backend, but I learned along the way that Node.js allows you to use js for both the front and backend.
