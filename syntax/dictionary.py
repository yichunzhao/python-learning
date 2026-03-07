import math

# create a mock dictionary with 3 key-value pairs, describing 3 person contacts
contacts = {
    ("mike", 23): "Mike 23 's contact",
    ("mike", 22): "Mike 22 's contact",
    ("jerry", 6): ["address", "phone number", "email"]
}

# iterate over values and print key
for key in contacts:
    print(key, ":", contacts[key])

for v in contacts.values():
    print(v)

for k, v in contacts.items():
    print(k, ":", v)

if ("mike", 23) in contacts:
    print("Mike 23 is in contacts")

# using for index in range to iterate contacts
for i in range(len(contacts)):
    key = list(contacts.keys())[i]
    value = contacts[key]
    print(key, ":", value)
# using while to iterate contacts
i = 0
while i < len(contacts):
    key = list(contacts.keys())[i]
    value = contacts[key]
    print(key, ":", value)
    i += 1


# define a function to calc circle area with radius as parameter
def circle_area(radius):
    return math.pi * radius * radius


# print area of circle with radius 5, and keep 2 decimal places
area = circle_area(5)
print("Area of circle with radius 5: {:.2f}".format(area))
