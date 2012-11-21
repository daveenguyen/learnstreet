#Happy Numbers Project
def happynum(num):
    '''Happy number is defined by following process:'''
    '''1) Starting with any positive integer, replace the number by the sum of the squares of its digits, and'''
    '''2) Repeat the process until the number equals 1 (where it will stay).'''
    '''If not, it loops endlessly in a cycle which does not include 1 (unhappy number!).'''

    sumList = [] # List to store sums that aren't 1
    n = str(num)

    while (True):
        sum = 0
        for i in range(len(n)):
            sum += int(n[i])**2 # adding the square of the digits

        if sum == 1:	# Sum is 1! Happy!
            return "Happy Number"

        for x in range(len(sumList)):
            if sum == sumList[x]:         # Check if sum is already in list.
                return "Unhappy Number"   # If it is return "Unhapy Number"

        sumList.append(sum) # sum not in list. Add to list.
        n = str(sum)