#user defined function sum()
def sum(array):
    n=len(array)
    summation=0
    i = 0
    #using while loop...Python doesn't have a built-in do-while loop like some other languages (such as C or Java).
    while i < n:
        summation+=array[i]
        i += 1
    return summation

#user defined function average()
def average(array):
    n=len(array)
    summation=sum(array)
    return summation/n

# n: 5
# array: 1 2 3 4 5
# Step 1: Take the number of elements
n = int(input("Enter the number of elements in the array: "))

# Step 2: Take the elements of the array
array = list(map(int, input(f"Enter {n} elements separated by space: ").split()))
print("Summation:",sum(array))
print(f"Average: {average(array):.2f}")
