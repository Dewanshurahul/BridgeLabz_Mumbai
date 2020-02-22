fileName = input("Enter File Name")
def absolute_file_path(fileName):
    import os
    return os.path.abspath(fileName)
print("Absolute file path: ", absolute_file_path(fileName))