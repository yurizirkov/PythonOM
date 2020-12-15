def greet(name):
    return f"Hey {name}!"

print(greet('Dan'))
print(greet('Mattan'))

def concatenate(word_one, word_two):
    return word_one + word_two

print(concatenate('Dan', 'Ven'))

def age_in_dog_years(age):
    return age * 7

print(age_in_dog_years(34))

name = "Dan"

def print_different_name():
    name = "Chris"
    print(name)

print(name)
print_different_name()
print(name)