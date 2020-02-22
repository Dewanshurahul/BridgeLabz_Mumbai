import array
class Array:

    def show(self,arr):
        for index in range(len(arr)):
            print(arr[index],end=" ")
        print()

    # def reverse(self,arr):
    #     last = len(arr)-1
    #     arrr = array.array('i',[])
    #     while last >= 0:
    #         arrr.append(arr[last])
    #         last -= 1
    #     return arrr

    def reverse(self,arr):
        index = 0
        last = len(arr)-1
        while index < len(arr)//2:
            t = arr[index]
            arr[index] = arr[last]
            arr[last] = t
            index += 1
            last -= 1
        return arr


    def occurence(self,element,arr):
        count = 0
        for index in range(len(arr)):
            if element == arr[index]:
                count += 1
        return count

    # def removeFirstOccurence(self,element,arr):
    #     for index in range(len(arr)):
    #         if element == arr[index]:
    #             aray = ([])
    #             ind = 0
    #             i = 0
    #             while ind < len(arr):
    #                 if ind == index:
    #                     ind += 1
    #                     continue
    #                 aray[i] = arr[ind]
    #                 ind += 1
    #                 i += 1
    #         return aray
    #     return arr

    def removeFirstOccurence(self,element,arrayOfElement):
        flag = 0
        newArr = array.array(arrayOfElement.typecode,[])
        for index in range(len(arrayOfElement)):
            if element == arrayOfElement[index] and flag == 0:
                flag = 1
            else:
                newArr.append(arrayOfElement[index])
        return newArr


a = Array()
arr = array.array('i',[12, 47, 78, 12, 65, 47, 37, 12,42])
a.show(arr)
a.show(a.removeFirstOccurence(47,arr))