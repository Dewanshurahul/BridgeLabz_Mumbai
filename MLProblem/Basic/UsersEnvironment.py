import os
class UserEnvironment:
    def userEnvironment(self):
        return os.environ

u = UserEnvironment()
print(u.userEnvironment())