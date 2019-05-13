#!/usr/bin/env python3

my_list = ["192.168.0.5", 5060, "UP"]

print("First item (IP): "  + my_list[0] )
print("Second iten (port): " + str(my_list[1]))

new_list = [ 5060, "80", 55, "10.0.0.1", "10.0.0.2", "ssh" ]

print(f"This ip: {new_list[3]} and this port: {new_list[0]}")

