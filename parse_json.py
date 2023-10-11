import json

# JSON to "Python":
person_info = '{"name":"Juliana", "age":24, "city":"Whatever"}'

# Parse person_info:
parse_info = json.loads(person_info)

# Print the parsed info but it will be a python dictionary(easy to access(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧):
print(parse_info["name"])

# "Python" to JSON
person_info = {"name": "Juliana", "age": 24, "city": "Whatever"}

# Converting into JSON
parse_info = json.dumps(person_info)

# Print the results (is a JSON string):
print(parse_info)

