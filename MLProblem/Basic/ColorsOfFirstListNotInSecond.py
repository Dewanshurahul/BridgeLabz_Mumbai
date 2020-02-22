from builtins import range
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
colorlist1 = tuple(color_list_1)
colorlist2 = tuple(color_list_2)
for color1Index in range(len(color_list_1)):
    for color2Index in range(len(color_list_2)):
        if colorlist1[color1Index] == colorlist2[color2Index]:
            break
    else:
        print(colorlist1[color1Index], end=" ")
