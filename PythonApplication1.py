def isLeapYear(newYear):
    if (newYear%4==0 and newYear%100!=0)\
        or (newYear%400==0):
        return True
    else:
        return False

def main():
    for i in range(0,3):
        x=int(input())
        if isLeapYear(x):
            print("The ",x," is leap year.")
        else:
            print( "The ",x," isn't leap year.")
main()
