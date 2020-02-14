name = input("Enter your Name: ")
givenString = "Hello <<UserName>>, How are you?"
requiredString = givenString.replace("<<UserName>>", name)
print(requiredString)
