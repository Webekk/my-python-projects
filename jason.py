import json
# Matter of fact i didn't knew there were so little functions in the json module
# And the second thing i need to watch out in that is the function keywords
# dump is a completely different function the DUMPS
# json.dump() method can be used for writing to JSON file.
# json.dumps() method can convert a Python object into a JSON string.

sample_data = {"Name": "Jasmine", "age": 20, "height": 70, "weight": 100}
dict_to_json = json.dumps(sample_data, sort_keys=True, indent=4) # Converting the dictionary to json
# Printing the converted dictionary in json
print(dict_to_json)
# Printing the dicitonary
print(sample_data)
