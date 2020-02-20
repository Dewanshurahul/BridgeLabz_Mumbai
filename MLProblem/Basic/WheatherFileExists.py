import pathlib
print("path example: /home/admin1/Desktop/BridgeLabz_Python/Basic/Factors.py")
path = input("Enter the Correct Path to find the File Exists Or Not: ")
file = pathlib.Path(path)
if file.exists():
    print ("File exist")
else:
    print ("File not exist")