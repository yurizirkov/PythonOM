answer = input("Do you want to hear a joke?")

#affirmative_responses = ["Yes", "yes", "y"]

#negative_responses = ["No", "no", "n"]

#if answer.lower() in affirmative_responses:
    #print("I am against picketing, but I do not know how to show it.")

#elif answer.lower() in negative_responses:
    #print("Fine")



#if answer == "Yes" or answer == "yes":
	#print("I am against picketing, but I do not know how to show it.")

#elif answer == "No":
    #print("Fine.")


if "y" in answer.lower():
    print("I am against picketing, but I do not know how to show it.")

elif "n" in answer.lower():
    print("Fine.")

else:
    print("I do not understand.")