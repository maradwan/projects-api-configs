from flask import Flask, request, jsonify
import re
from os import environ as env

# Get environment, or set to development by default
app_env = env.get('FLASK_ENV')
if not app_env:
    raise ValueError("No FLASK_ENV has been set, ex. export FLASK_ENV=development")


# Settings applied to specific environments
if app_env == 'production':
    DEBUG = False

elif app_env == 'development':
    DEBUG = True

# Init app
app = Flask(__name__)

holds = []

# Create a Config
@app.route('/configs', methods=['POST'])
def add_config():
  name = request.json['name']
  data = request.json['data']

# If you want to have a unique name, uncomment this block

#  for hold in holds:
#      if (name == hold['name']):
#          return "{} already exists.".format(name),400


  holds.append({"name": name, "data": data })
  return jsonify(name,data)

# Get All Configs
@app.route('/configs', methods=['GET'])
def get_configs():
  return jsonify(holds)

# Get Single Config
@app.route('/configs/<name>', methods=['GET'])
def get_config(name):
    for hold in holds:
        if (name == hold['name']):
            return jsonify(hold)

    return "{} is not exists.".format(name),400


# Update a Config
@app.route('/configs/<name>', methods=['PUT', 'PATCH'])
def update_config(name):
    name = request.json['name']
    data = request.json['data']

    for hold in holds:
         if (name == hold['name']):
             get_index= holds.index(hold)
             holds[get_index]= {"name": name, "data": data }
             return jsonify(holds[get_index])

    return "{} is not exists.".format(name),400


# Delete Config
@app.route('/configs/<name>', methods=['DELETE'])
def delete_config(name):
     for hold in holds:
         if (name == hold['name']):
             holds.remove(hold)
             return jsonify(name)
     return "{} is not exists.".format(name),400


def search(name):
    for hold in holds:
        if (name == hold['name']):
            get_index= holds.index(hold)
            return holds[get_index]

# Search Config
@app.route('/search', methods=['GET'])
def search_config():
    name = request.args.get('name')
    all_args = request.full_path
      
    reg = re.search('data\.(.*)\=(.*)', all_args, re.IGNORECASE)
    
    key = reg.group(1)
    data = reg.group(2)
   
    new_holds = []
    new_values = []

    try:
        for hold in holds:
            if (name == hold['name']):
                get_index= holds.index(hold)
                new_holds.append(holds[get_index])


        for i in range(len(new_holds)):
            if (str(new_holds[i].get('data').get(key)) == data):
                new_values.append(new_holds[i])

        return jsonify(new_values)

    except:
        return "name {} and data {} are not exists.".format(name,data),400




# Run Server
if __name__ == '__main__':
  app.run(debug=DEBUG, port=env.get("SERVE_PORT"))
