#1 Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(num):
    new=[]
    for x in range(num, -1, -1):
        new.append(x)
    return new
print(countdown(5))

#2 Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_and_return(list):
    print(list[0])
    return(list[1])
print(print_and_return([1,2]))

#3 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_plus_length(list):
    a = list[0]
    b = len(list)
    return a+b
print(first_plus_length([1,2,3,4,5]))

#4 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def values_greater_than_second(list):
    newList=[]
    greater = 0
    for x in range(len(list)):
        if list[x] > list[1]:
            newList.append(list[x])
            greater += 1
        if len(list) <=2:
            return False
    print(len(newList))
    return newList
print(values_greater_than_second([5,2,3,2,1,4]))

#5
def thisLenThatVal(size, value):
    newList=[]
    for x in range(size):
        newList.append(value)
    return newList
print(thisLenThatVal(4, 7))
