class Dictionary(dict):
    def sortAsc(self, dictionary):
        for index in list(dictionary):
            for ind in list(dictionary):
                if dictionary.get(index) < dictionary.get(ind):
                    t = dictionary.get(index)
                    dictionary[index] = dictionary.get(ind)
                    dictionary[ind] = t
        return dictionary


d = Dictionary()
detail = {"name": 35, "age": 23, "x": 26}
print(d.sortAsc(detail))
