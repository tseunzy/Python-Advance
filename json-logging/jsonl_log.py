
import json
print("=============Reading from String===================")

# JSON string
json_strings = '''{
  "employees": [
    {
      "id": 1,
      "name": "John",
      "department": "IT",
      "salary": 50000
    },
    {
      "id": 2,
      "name": "Sarah",
      "department": "HR",
      "salary": 45000
    }
  ],
  "company": "TechCorp",
  "location": "Abuja"
}
'''

# Convert JSON string to Python dictionary  # 'loads' = LOAD String
data = json.loads(json_strings) #this is use to convert a json string to python

print(data)    
print(type(data))           # <class 'dict'>
print(data["location"])     # 'Abuja'
print(data['employees'])



for emp in data['employees']:
    print(emp["name"])          # 'John'  'Sarah'
#     del emp["salary"]

# print(data['employees'])


print("=============Reading from File===================")

# Read JSON file
with open("Nigerian_states.json", 'r') as file:
    state_data = json.load(file)  # 'Load' = Load from file

# Access nested data
print(state_data["languages"])    # ['English', 'Hausa', 'Yoruba', 'Igbo']

# Access array data
for reg in state_data["regions"]:
    print(reg["name"])
    # for state in reg["states"]:
    #     print(state["name"])



print("=============Writing to Json String===================")

# Python dict to JSON string
# Python dictionary
python_dict = {
    "name": "Bob",
    "age": 35,
    "married": True,
    "children": None,
    "hobbies": ["reading", "swimming"]
}

# Convert Python dict to JSON string
json_string = json.dumps(python_dict, indent=2, sort_keys=True)  # 'dumps' = DUMP to String

print(json_string) # using the INDENT to Human Readable)


print("=============Writing to Json File===================")
# Writing to File
data = {
    "product": "Laptop",
    "price": 999.99,
    "in_stock": True,
    "specs": ["16GB RAM", "512GB SSD", "Intel i7"]
}


with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)  # 'dump' = DUMP to file



print("=============Writing to Json File===================")
# Writing to File
with open("Nigerian_states.json", "r") as k:
    cont = json.load(k)
with open('new_state.json', 'w', encoding='utf-8') as file:
    json.dump(cont, file, indent=4, sort_keys=True)  # 'dump' = DUMP to file
# Save data to file




# json.loads(string)	  Read JSON from string   - returns Python object dict/list, When you have JSON as a string
# json.load(file)	      Read JSON from file - returns Python object dict/list
# json.dumps(obj)	      Convert Python object to JSON string  - Get JSON as string for display
# json.dump(obj, file)	Write Python object to file as JSON - Save data to file












