import datetime
class GetSystemTime:
    def systemTime(self):
        return datetime.datetime.now().strftime("%H:%M:%S")

g = GetSystemTime()
print(g.systemTime())