import re

# First Letter of First Name is UPPER_CASE
firstName = input("Enter first Name")
if (re.match("^[A-Z]",firstName)):
    print("First Letter is UPPER_CASE ",firstName)
else:
    print("Enter FIRST letter of First Name as UPPER_CASE")
# First Letter of Last Name is UPPER_CASE
lastName = input("Enter the Last Name: ")
if (re.match("^[A-Z]",lastName)):
    print("First Letter is UPPER_CASE ",lastName)
else:
    print("Enter First letter of Last Name as UPPERCASE!")

# E-mail ID is Valid or Not
email = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|org|net)"
mailID = input("Enter E-mail : ")
if(re.search(email, mailID)):
    print("Valid format for E-mail")
else:
    print("Invalid format for E-mail")

# Phone Number is valid or Not
mobile = "^((\+)?(\d{2}[-]))?(\d{10}){1}?$"
mobileNo = input("Enter a Mobile number: ")
if(re.search(mobile, mobileNo)):
    print("Mobile number is Valid!")
else:
    print("Invalid Mobile Number format")
    print("Enter Mobile Number as +xx-xxxxxxxxxx")

# Password had minimum 8 characters
password = input("Enter a Password: ")
count = '^.{8,}$'
pwdCheck = re.match(count, password)
if(pwdCheck):
    print("Correct Password", password)
else:
    print("Enter atleast 8 Character")

# Password has at least 8 characters and one UPPERCASE
password = input("Enter a Password: ")
pwd = "^(?=.*[A-Z])[a-zA-Z\d]{8,}$"
if(re.match(pwd, password)):
    print("Correct Password",password)
else:
    print("Enter Atleast charavter with one Upper_Case")

# Password has at least 8 characters, one UPPERCASE and one Number
password = input("Enter a Password: ")
passwd = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
if(re.match(passwd, password)):
    print("Correct Password",password)
else:
    print("Input in Correct Format")
# Password has at least 8 characters, one UPPERCASE, one Number and one Special Character
password = input("Enter a Password: ")
pwd = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
if(re.match(pwd, password)):
    print("Correct Password",password)
else:
    print("Enter Proper Valid Password")