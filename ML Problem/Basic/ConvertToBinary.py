class Binary:
    def binary(self,number):
        binary = ""
        while(number != 0):
            x = number % 2
            binary = str(x) + binary
            number //= 2
        length = 4 - (len(binary) % 4)
        for i in range(length):
            binary = "0" + binary
        return binary

number = int(input("Enter any number to get binary of it: "))
b = Binary()
print(b.binary(number))