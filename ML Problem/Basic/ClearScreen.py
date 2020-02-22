import subprocess
class ClearScreen:
    def clear(self):
        return subprocess.run("clear")

c = ClearScreen()
c.clear()