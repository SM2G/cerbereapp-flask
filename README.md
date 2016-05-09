# Cerbere App

## Installation
Cerbere App can be deployed on any small scale server meeting the following requirements:

### Requirements

+ alembic==0.8.6
+ Flask==0.10.1
+ Flask-Login==0.3.2
+ Flask-SQLAlchemy==2.1
+ Flask-WTF==0.12
+ itsdangerous==0.24
+ Jinja2==2.8
+ Mako==1.0.4
+ MarkupSafe==0.23
+ PyMySQL==0.7.2
+ python-editor==1.0
+ SQLAlchemy==1.0.12
+ Werkzeug==0.11.9
+ WTForms==2.1

```
$ virtualenv venv -p python3.5
$ source venv/bin/activate
$ pip install -f requirements.txt
$ cp config.py.sample config.py # and edit it
$ python runserver
```

## Features Roadmap
+ ~~Login/logout~~
+ Mysql database support
+ Account managment
+ Encrypted password storage
+ Add/remove/manage document models
+ Add/remove/manage profiles
+ Add/remove/manage employees
+ Add/remove/manage actual documents
+ Design a pretty Dashboard
+ E-mail sending
+ Upload document scans
+ Use Alembic for database migrations
+ Create guest accounts
+ Advanced guest accounts
