from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

base_url = f"https://{os.environ['REGION']}.api.ecourtdate.com/"

params = {
    "agency": os.environ['AGENCY']
}

@app.route("/clients", methods=["GET"])
def get_clients():

    headers = generateToken()

    if 'Authorization' not in headers:
        return jsonify({"error": "Invalid API token"}), 400

    params['slim'] = 'y'
    params['limit'] = 5
    params['search'] = request.args.get('search', None)

    response = requests.get(f"{base_url}v1/clients", params = params, headers = headers)

    return jsonify(response.json())

@app.route("/clients/<client_reference>", methods=["GET"])
def get_client(client_reference):

    headers = generateToken()

    if 'Authorization' not in headers:
        return jsonify({"error": "Invalid API token"}), 400

    response = requests.get(f"{base_url}v1/clients/{client_reference}", params = params, headers = headers)

    return jsonify(response.json())

@app.route("/clients", methods=["POST"])
def create_client():

    headers = generateToken()

    if 'Authorization' not in headers:
        return jsonify({"error": "Invalid API token"}), 400

    json = {
    "client_reference": "CA-123456789",
    "first_name": "alphonse",
    "last_name": "capone",
    "dob": "01/17/1899",
    "gender": "male",
    "type": "defendant",
    "email": "al.capone@gmail.com",
    "phone": "(111) 222-5555"
    }

    response = requests.post(f"{base_url}v1/clients", params = params, headers = headers, json = json)

    return jsonify(response.json())

@app.route("/clients/<client_reference>", methods=["PUT"])
def update_client(client_reference):

    headers = generateToken()

    if 'Authorization' not in headers:
        return jsonify({"error": "Invalid API token"}), 400

    json = {
    "group": request.json.get('group', '2B'),
    "middle_name": request.json.get('middle_name', 'gabriel')
    }

    response = requests.put(f"{base_url}v1/clients/{client_reference}", params = params, headers = headers, json = json)

    return jsonify(response.json())

@app.route("/clients/<uuid>", methods=["DELETE"])
def delete_client(uuid):

    headers = generateToken()

    if 'Authorization' not in headers:
        return jsonify({"error": "Invalid API token"}), 400

    response = requests.delete(f"{base_url}v1/clients/{uuid}", params = params, headers = headers)

    return jsonify(response.json())

def generateToken():

    response = requests.post(f"{base_url}oauth/token", json = set_token())

    if response.status_code != 201 or 'access_token' not in response.json():
        return 'failed'

    return {
    "Authorization": f"Bearer {response.json()['access_token']}"
    }

def set_token():

    return {
    "client_id": os.environ['CLIENT_ID'],
    "client_secret": os.environ['CLIENT_SECRET'],
    "grant_type": "client_credentials",
    "scope": "*"
    }

def apiHeaders(token):

    return {
    "Authorization": f"Bearer {token['access_token']}"
    }