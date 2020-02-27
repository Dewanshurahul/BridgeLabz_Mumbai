import json

# Used for Writing the Data onto the JSON file
def write_json(data, filename):
    with open(filename, 'w') as addBook:
        json.dump(data, addBook, indent=4)

# Return True if passed Element is Present is Present else return False
def elementExists(element):
    with open('addressBook.json') as addressBook:
        dataOnFile = json.load(addressBook)
        for datas in dataOnFile["personalDetail"]:
            if datas.get("firstname") == element:
                return True
    return False

# To add New Entry into the JSON File
def add():
    firstName = input("Enter Your First_Name: ")
    lastName = input("Enter Your Last_Name: ")
    address = input("Enter Your Address: ")
    city = input("Enter Your CITY: ")
    state = input("Enter Your State: ")
    zip = str(input("Enter your ZIP Number: "))
    phoneNumber = str(input("Enter your Phone Number: "))
    try:
        addressDetail = {
            "firstname": firstName,
            "lastName": lastName,
            "address": address,
            "city": city,
            "state": state,
            "zip": zip,
            "phoneNumber": phoneNumber
        }
        with open('addressBook.json') as addressBook:
            dataOnFile = json.load(addressBook)
            temp = dataOnFile["personalDetail"]
            temp.append(addressDetail)
        write_json(dataOnFile, 'addressBook.json')
        print("Data Saved !!!")
    except:
        addressDetail = {
            "personalDetail": [
                {
                    "firstname": firstName,
                    "lastName": lastName,
                    "address": address,
                    "city": city,
                    "state": state,
                    "zip": zip,
                    "phoneNumber": phoneNumber}
            ]}
        write_json(addressDetail, 'addressBook.json')
        print("Data Saved !!!")


# def sortByZip():
#     with open('addressBook.json') as sort:
#         data = json.load(sort)
#     for datas in data["personalDetail"]:
#         for nextData in data["personalDetail"]:
#             if datas.get("zip") > datas.get("zip"):
#                 temp = datas
#                 datas = nextData
#                 nextData = temp

# Search for Data Based on FirstName or MobileNumber or LastName of the Entry
def search(element):
    with open('addressBook.json') as addressBook:
        dataOnFile = json.load(addressBook)
    for datas in dataOnFile["personalDetail"]:
        if element == datas.get("firstname") or element == datas.get("phoneNumber") or element == datas.get("lastName"):
            print(datas)

# Delete a Object from JSON file based on FirstName
def delete(element):
    if elementExists(element) == False:
        print("Data Not Present")
        return None
    with open('addressBook.json') as addressBook:
        dataOnFile = json.load(addressBook)
    temp = []
    for datas in dataOnFile["personalDetail"]:
        if element == datas.get("firstname"):
            pass
        else:
            temp.append(datas)
    dictionary = {"personalDetail": temp}
    write_json(dictionary, 'addressBook.json')
    print("Data Deleted")

# delete("kiran")
search("Dewanshu")