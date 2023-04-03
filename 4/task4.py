import json
import datetime


def change_data(data:dict, value_in:str):

    for key, value in data.items():
        if isinstance(value, dict):
            data[key] = change_data(data[key], value_in)
        if key == value_in:
            data[key] = datetime.datetime.now().isoformat()
    return data  

def change_updated_for_data():    
    with open('data.json', 'r') as f:
        data = json.load(f)

    new_data = change_data(data, 'updated')

    with open('data.json', 'w') as f:
        json.dump(new_data, f, indent=4)

change_updated_for_data()