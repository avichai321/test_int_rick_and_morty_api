#!/usr/bin/python

from flask import Flask, request, jsonify
import requests
import csv

app = Flask(__name__)

api_endpoint = "https://rickandmortyapi.com/api/character"

def get_accurate_list(data_list):
    resulted_list = []
    for d in data_list:
        d_origin = d['origin']
        if (d['status'] == 'Alive') and (d['species'] == 'Human'):
            if d_origin['name'] is not None and 'Earth' in d_origin['name']:
                resulted_list.append(d)
    return resulted_list

@app.route('/fetch_char', methods=['GET'])
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

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "Server is running"}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
