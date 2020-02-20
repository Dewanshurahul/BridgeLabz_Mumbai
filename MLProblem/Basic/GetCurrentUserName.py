import getpass
class CurrentUser:
    def getName(self):
        return getpass.getuser()

c = CurrentUser()
print(c.getName())