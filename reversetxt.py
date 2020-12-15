def uppercase_and_reverse(text): # this is a function
    uppercase_text = text.upper() # this is a string 
    return uppercase_text[::-1] 

def reverse(text):
    return text[::1]


print(uppercase_and_reverse('text to be uppercase and reversed'))

print(reverse('text to be uppercase and reversed'))