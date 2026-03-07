# tuple as dictionary key
p1 = ("mike", 23)
p2 = ("mike", 22)

# dictionary with tuple keys
contacts = {p1: "Mike 23 's contact", p2: "Mike 22 's contact"}

print(contacts[p2])

# list as dictionary value
c = ["address", "phone number", "email"]
# add c to contacts with key ("jerry", 6)
contacts[("jerry", 6)] = c

print(contacts[("jerry", 6)])


