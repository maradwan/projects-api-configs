
## Requirements

# Install Flask
* pip install flask


## Run

    # To define Serving Port default 5000
    
    $ export SERVE_PORT=5000
    
    # For Production Environment 

    $ export FLASK_ENV=production
    
    # For Development Environment

    $ export FLASK_ENV=development

    # To Run

    $ python app.py


## Add new data 
    $ curl --request POST --url 'http://127.0.0.1:5000/configs' -H 'content-type: application/json' --data '{ "name": "database", "data": { "ip": "192.168.1.1", "hostname": "eg001", "uptime": 7.3, "env": "prod" }}'
    $ curl --request POST --url 'http://127.0.0.1:5000/configs' -H 'content-type: application/json' --data '{ "name": "database", "data": { "ip": "192.168.1.2", "hostname": "eg002", "uptime": 10, "env":  "prod"  }}'
    $ curl --request POST --url 'http://127.0.0.1:5000/configs' -H 'content-type: application/json' --data '{ "name": "database", "data": { "ip": "192.168.1.3", "hostname": "eg003", "uptime": 244, "env": "dev" }}'
    $ curl --request POST --url 'http://127.0.0.1:5000/configs' -H 'content-type: application/json' --data '{ "name": "web", "data": { "ip": "192.168.1.4", "hostname": "eg004", "uptime": 400, "env": "prod"  }}'
    $ curl --request POST --url 'http://127.0.0.1:5000/configs' -H 'content-type: application/json' --data '{ "name": "web", "data": { "ip": "192.168.1.5", "hostname": "eg005", "uptime": 544, "env": "prod"  }}'
    $ curl --request POST --url 'http://127.0.0.1:5000/configs' -H 'content-type: application/json' --data '{ "name": "web", "data": { "ip": "192.168.1.6", "hostname": "eg006", "uptime": 344, "env": "dev"  }}'

## Uptdate data
    $ curl  --request PUT --url 'http://127.0.0.1:5000/configs/database' -H 'content-type: application/json' --data '{ "name": "database", "data": { "ip": "192.168.1.100", "hostname": "eg001", "uptime": 550, "env": "testing" }}'

## Delete data
    $ curl  --request DELETE --url 'http://127.0.0.1:5000/configs/database'

## Get all data 
    $ curl  --request GET --url 'http://127.0.0.1:5000/configs'

## Get Spesfic Name
    $ curl  --request GET --url 'http://127.0.0.1:5000/configs/database'

## Search Query
    $ curl --request GET --url 'http://127.0.0.1:5000/search?name=database&data.env=prod'
    $ curl --request GET --url 'http://127.0.0.1:5000/search?name=web&data.env=dev'


## Note:
  Assumed name is not unique, if you want to have a unique name remove commented block from line 31-33 in app.py
