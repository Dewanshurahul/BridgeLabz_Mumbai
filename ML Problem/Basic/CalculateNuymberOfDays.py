from datetime import date
firstDate = input("Enter First Date in Format yyyy/mm/dd")
secondDate = input("Enter Second Date in Format yyyy/mm/dd")
intermediateFirstDate = firstDate.split("/")
intermediateSecondDate = secondDate.split("/")
date1 = date(int(intermediateFirstDate[0]), int(intermediateFirstDate[1]), int(intermediateFirstDate[2]))
date2 = date(int(intermediateSecondDate[0]), int(intermediateSecondDate[1]), int(intermediateSecondDate[2]))
day = date2 - date1
print(str(day.days)+" days")