#!/usr/bin/python

from flask import Flask, request, jsonify ,render_template_string
import requests
import csv

rick_and_morty = Flask(__name__)

api_endpoint = "https://rickandmortyapi.com/api/character"

@rick_and_morty.route('/')
def home():
    return render_template_string('''
    <html>
    <head>
        <title>Flask App</title>
    </head>
    <body>
        <h1>Welcome to Rick and Morty api app</h1>
        <h2>Made by Avichai Dahan</h2>
        <button onclick="window.location.href='/healthcheck';">Health Check</button>
        <button onclick="window.location.href='/fetch_char';">Fetch Characters</button>
    </body>
    </html>
    ''')

def get_accurate_list(data_list):
    resulted_list = []
    for d in data_list:
        d_origin = d['origin']
        if (d['status'] == 'Alive') and (d['species'] == 'Human'):
            if d_origin['name'] is not None and 'Earth' in d_origin['name']:
                resulted_list.append(d)
    return resulted_list

@rick_and_morty.route('/fetch_char', methods=['GET'])
def fetch_char():
    main_params = {
        'status': 'Alive',
        'species': 'Human',
        'origin': {
            'name': 'Earth'
        }
    }

    try:
        response = requests.get(api_endpoint, params=main_params)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()
        character_data = get_accurate_list(data['results'])

        csv_file = 'results.csv'
        fields = ['Name', 'Location', 'Image']
        final_list= []
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)

            writer.writerow(fields)

            for char_a in character_data:
                writer.writerow([char_a['name'], char_a['location']['name'], char_a['image']])
                final_list.append([{'Name':char_a['name']}, {'Location':char_a['location']['name']}, {'image': char_a['image']}])


        return jsonify(final_list)

    except requests.exceptions.HTTPError as errh:
        return jsonify({"error": f"HTTP Error: {errh}"}), 500
    except requests.exceptions.ConnectionError as errc:
        return jsonify({"error": f"Error Connecting: {errc}"}), 500
    except requests.exceptions.Timeout as errt:
        return jsonify({"error": f"Timeout Error: {errt}"}), 500
    except requests.exceptions.RequestException as err:
        return jsonify({"error": f"Oops: Something Else: {err}"}), 500

@rick_and_morty.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "Server is running"}), 200

if __name__ == '__main__':
    rick_and_morty.run(host='0.0.0.0', port=8080)
