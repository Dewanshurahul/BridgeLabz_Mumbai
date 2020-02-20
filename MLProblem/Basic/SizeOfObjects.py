import sys
class SizeOfObjects:
    def sizeObject(self,object):
        return sys.getsizeof(object)


string = "Dewanshu Rahul"
s = SizeOfObjects()
print(s.sizeObject(string))