class Maximum:
    def max(self,sequence):
        sequence = list(sequence)
        if len(sequence) != 0:
            max = sequence[0]
        else:
            return None
        for index in range(1, len(sequence)):
            if max < sequence[index]:
                max = sequence[index]
        return max

m = Maximum()
lst = {5, 9, 33, 4}
print(m.max(lst))
