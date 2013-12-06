from flask import Flask
import flask
import json
import logging
import os
import uuid
from flask_helper import crossdomain


app = Flask(__name__, static_url_path='')
logging.basicConfig(level=logging.INFO)

@app.route('/')
@crossdomain(origin='*')
def root():
  return app.send_static_file('index.html')


@app.route("/apptime/devices/<id>/usage", methods=["GET", "POST"])
@crossdomain(origin='*')
def usage(id):
    if flask.request.method == 'GET':
        return flask.jsonify(**{ "usage": [
                       {"category": "Game", "apps" : [
                              {"name": "Super mario brothers"},
                              {"name": "Frogger"} ]
                       },
                       {"category": "Social", "apps" : [
                              {"name": "Facebook"},
                              {"name": "Twitter"},
                              {"name": "Snapchat"},
                               ]
                       }
                       ]
        })
    if flask.request.method == 'POST':
        logging.info("Received %s", flask.request.data)
        return flask.jsonify(**{})

@app.route("/apptime/device", methods=["POST"])
@crossdomain(origin='*')
def device():
    data = flask.request.get_json(force=True)
    logging.info("Registering new device for %s", data["name"])
    return flask.jsonify(**{"id":str(uuid.uuid4())})

@app.route("/apptime/users/<username>/devices", methods=["GET"])
@crossdomain(origin='*')
def user_devices(username):
    return flask.jsonify(**{'devices':[{'device_name': 'Galaxy Nexus',  'id': '123'}]})


def start_server():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    start_server()
