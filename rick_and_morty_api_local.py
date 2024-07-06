import requests
import csv

api_endpoint = "https://rickandmortyapi.com/api/character"

# Define the parameters
main_params = {
    'status': 'Alive',
    'species': 'Human',
    'origin': {
        'name': 'Earth'
     }
}



def get_accurate_list(data_list):
    resulted_list = []
    for d in data_list:
        d_origin = d['origin']
        if (d['status'] == 'Alive') and (d['species'] == 'Human'):
            if d_origin['name'] != None and 'Earth' in d_origin['name']:
                resulted_list.append(d)
    return resulted_list


response = requests.get(api_endpoint, params=main_params)
# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    character_data = get_accurate_list(data['results'])
    # Print the data (or process it as needed)
    print(data)

    csv_file = 'results.csv'
    fields = ['Name', 'Location', 'Image']
    final_list = []
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(fields)

        # Write the data row
        for char_a in character_data:
            writer.writerow([char_a['name'], char_a['location']['name'], char_a['image']])
            final_list.append([{'Name':char_a['name']}, {'Location':char_a['location']['name']}, {'image': char_a['image']}])
        file.close()
    print(f"Data has been written to {csv_file}")

else:
    # Print the error message
    print(f"Error: {response.status_code}, {response.text}")
