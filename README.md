# Cerbere App

## Installation
Cerbere App can be deployed on any small scale server meeting the following requirements:

### Requirements

+ Flask==0.10.1
+ itsdangerous==0.24
+ Jinja2==2.8
+ MarkupSafe==0.23
+ PyMySQL==0.7.2
+ Werkzeug==0.11.9

```
$ bundle install
$ cp config/application.yml.sample config/application.yml # and edit it
$ rake db:migrate
$ rake db:seed
```

## Execution

work in progress

```
$ python cerbereapp.py
```

## Features Roadmap
+ ~~Logging in/out~~
+ Mysql database support
+ Encrypted password storage
+ 
+ Add/remove employees
+ Add/remove employees

+ Add/remove employees
+ Add/remove profiles
+ Dashboard
