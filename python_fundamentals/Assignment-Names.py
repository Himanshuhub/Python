# Assignment: Names
# # Part 1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def part1(l):
  for i in l:
    # print i
    print i['first_name'], i['last_name']

part1(students)

# part 2

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def Part(users):
  for key in users:
    print key
    # print users
    counter = 0
    for person in users[key]:
      # print person['first_name']
      counter += 1
      # print counter
      length = len(person['first_name']) + len(person['last_name'])
      # print length
      print str(counter) + " - "+ person['first_name'], person['last_name'] + " - ", str(length)

Part(users)
