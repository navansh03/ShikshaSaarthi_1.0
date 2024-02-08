import json

# Read the UTF-16LE encoded JSON file
with open('data.json', 'r', encoding='utf-16-le') as f:
    data = f.read()

# Remove the UTF-16LE BOM (Byte Order Mark)
if data.startswith('\ufeff'):
    data = data[1:]

# Convert the JSON data to Python objects
json_data = json.loads(data)

# Write the data back to a UTF-8 encoded JSON file
with open('data2.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)


print('succesfully done converting')