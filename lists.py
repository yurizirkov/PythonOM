the_count = [1,2,3,4,5]
stocks = ["AAPL", "GOOG", "TSLA"]
random = ["Puppies", 55, "Ant", ["list inside list"]]

# this for-loop goes through a list

for number in the_count:
    print("this is count", number)

    #same as above

for stock in stocks:
    print("stock ticker:", stock)

#we can go through mixed lists too
#i called it i (short for item) since i dont konw what is in it

for i in random:
    print("here is a random thing:", i)

    #we can also build lists

people = []

people.append("Dan")
people.append("Mel")
people.append("Zeph")

#now we can print them out too
print(people)

#and remove some 
people.remove("Dan")
print(people)

for person in people:
    print("person is", person)





