# Cerbere App

## Installation
Cerbere App can be deployed on any small scale server meeting the following requirements:

### Requirements

+ Flask==0.10.1
+ Flask-Login==0.3.2
+ Flask-SQLAlchemy==2.1
+ Flask-WTF==0.12
+ itsdangerous==0.24
+ Jinja2==2.8
+ MarkupSafe==0.23
+ PyMySQL==0.7.2
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
+ Add/remove employees
+ Add/remove profiles
+ Add/remove document models
+ Dashboard
+ Upload document scans
+ Create guest accounts
+ Advanced guest accounts
