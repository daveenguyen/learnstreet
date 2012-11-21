#Basic bubble sort project
def bubble_sort(n):
    "The goal is to sort a series of numbers in ascending order. The procedure of a bubble sort"
    "is to compare adjacent numbers in pairs, two at a time, and swap the positions of the two"
    "numbers if a larger number comes before a shorter one. After the first pass through the series"
    "of numbers, the process repeats the pass through the entire list over and over again until there"
    "are no more number swaps needed.'"
    needSwap = True
    while needSwap:
        needSwap = False
        for i in range(len(n)-1):
            if n[i] > n[i+1]:
                needSwap = True
                buf = n[i]
                n[i] = n[i+1]
                n[i+1] = buf
    return n