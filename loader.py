import json

def pretty_print(json_data):
    for key, val in json_data.items():
        print(f'{key}: {val}')

with open('sample_output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

pretty_print(data)