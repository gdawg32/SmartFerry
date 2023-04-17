import time
import json

# Define the path to the JSON file
json_file_path = "C:\\Users\\Dell\\Documents\\smart ferry\\SmartFerry\\home\\static\\js\\data.json"

print("script run")

while True:
    # Load the JSON data from the file
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Update the latitude and longitude values
    data['latitude'] -= 0.001
    data['longitude'] -= 0.001

    # Write the updated JSON data to the file
    with open(json_file_path, 'w') as f:
        json.dump(data, f)

    # Wait for 5 seconds before updating the JSON data again
    time.sleep(2)
