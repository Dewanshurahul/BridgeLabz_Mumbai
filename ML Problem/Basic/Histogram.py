class Histogram:
    def histogram(self, lst):
        for index in range(len(lst)):
            print("* "*lst[index])

h = Histogram()
lst = [2,4,10,1]
h.histogram(lst)