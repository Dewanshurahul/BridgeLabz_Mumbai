class EmptyVariable:
    def empty(self,variable):
        return type(variable)()

e = EmptyVariable()
lst = (5, 4, 55)
print(e.empty(lst))
print(type(lst)())