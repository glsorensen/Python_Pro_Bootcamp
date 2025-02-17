import json
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
json_string = json.dumps(programming_dictionary)

print(json_string)