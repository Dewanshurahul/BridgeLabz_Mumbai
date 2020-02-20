import sys
class RecursionLimit:
    def limit(self):
        return sys.getrecursionlimit()

r = RecursionLimit()
print(r.limit())