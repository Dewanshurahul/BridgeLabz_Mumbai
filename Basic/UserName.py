# Replacing a part of given String with desired content using regular expression.
import re
name = input("Enter your Name: ")
givenString = "Hello <<UserName>>, How are you?"
requiredString = re.sub("<<UserName>>", name, givenString)
#requiredString = givenString.replace("<<UserName>>", name)
print(requiredString)
