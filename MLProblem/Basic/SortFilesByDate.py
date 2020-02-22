import glob
import os
class Sort_FilesByDate:
    def sortFiles(self):
        files = glob.glob("*.py")
        files.sort(key=os.path.getmtime)
        print("\n".join(files))
s1 = Sort_FilesByDate()
s1.sortFiles()