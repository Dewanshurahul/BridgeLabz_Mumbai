import os
class SystemCommand:
    def systemCommand(self,command):
        return os.system(command)

s = SystemCommand()
s.systemCommand('ls -al')