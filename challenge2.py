#!/usr/bin/env python3

first_list = []
first_dict = {"first_name":"monty", "last_name":"python", "actions":["scooter", 2, "Moscow"]}

print(f'in {first_dict["first_name"]} {first_dict["last_name"]}, Eric Idle rode a {first_dict["actions"][0]} {first_dict["actions"][1]} {first_dict["actions"][2]}') 
first_list.extend(['horse', 'to', 'the Holy Grail'])

# print (first_list)

first_dict.update ({"actions":first_list})

# print (first_dict)

print(f'in {first_dict["first_name"]} {first_dict["last_name"]}, Eric Idle rode a {first_dict["actions"][0]} {first_dict["actions"][1]} {first_dict["actions"][2]}') 

