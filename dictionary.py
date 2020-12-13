# states = ['NY', 'PA', 'CA']
# states = ['New York', 'Pennsylvania', 'California']
# states = ['New York', 'NY', 'Pennsylvania', 'PA', 'California', 'CA']

states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}

#          key   value  -- Dictionaries are key and value pair. you get them using
#                           the key

print(states ['NY'])

print(type(states))

print(states.get('FL', 'Not found'))
print(states.get('NY', 'Not found'))


user = {'name': 'Dan', 'height': 170, 'hair': 'Brown',}

blog_post = {'title': '11 Great uses for Dictionaries', 'body': 'Fat people use stuff'}

print(user['name'])
print(blog_post['title'])

#list in dictionary

animal_sounds = {
    "cat": ["meow", "purr"],
    "dog": ["woof", "bark"],
}

mattan = {'name': 'Mattan', 'height': 70, 'shoe size': 10.5, 'hair': 'Brown', 'eyes': 'Brown'}

chris = {'name': 'Chris', 'height': 68, 'shoe size': 10, 'hair': 'Brown', 'eyes': 'Brown'}

sarah = {'name': 'Sarah', 'height': 72, 'shoe size': 8, 'hair': 'Brown', 'eyes': 'Brown'}

people = [mattan, chris, sarah]

print(people)

for person in people:
    print(person.get('height'))