weekend = {"Sun": "Sunday", "Mon": "Monday"} #literal notation
# print weekend

capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
capitals["dnk"] = "Copoooooo"

# print capitals
# print weekend["Sun"]
# print capitals["svk"]

# for i in capitals:
#     print i

# to print Keys
# for key in capitals.iterkeys():
#     print key

# To print values
# for val in capitals.itervalues():
#     print val
# # To print all keys and values
# for key,data in capitals.iteritems():
#     print key, "=", data
#
context = {
    'questions': [
    {'id': 1, 'content': 'light'},
    {'id': 2, 'content': 'shrink'},
    {'id': 3, 'content': 'apt'},
    {'id': 4, 'content': 'cars'}
    ]
}
# print context


# To iterate the values, we can use the nested for loop:
# for key, data in context.items():
#     for value in data:
#         print "Question #", value["id"], ":", value["content"]
#         print "----"

# data = {"house": "haus", "cat": "Katze", "red": "rot"}
# print data.items()
# print data.keys()
# print data.values()

# Dictionaries from Lists
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

country_specialities = zip(countries, dishes)
# print country_specialities

country_specialities_dict = dict(country_specialities)
print country_specialities_dict
