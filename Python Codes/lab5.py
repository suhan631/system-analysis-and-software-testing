n=int(input("Please Enter a number: "))
print("Evaluating factorial of a number using for loop: ")
print("-------------------------------------------------")
fact=1
for i in range(1,n+1):
   prev=fact
   fact = i*fact
   # To verify the factorial
   print(f"In {i} iteration factorial is {prev} X {i} = {fact}")
print(f"Factorial of {n} using for loop: {fact}")
print('\n')
# Calculating factorial using a while loop
print("Evaluating factorial of a number using while loop: ")
print("---------------------------------------------------")
fact = 1
i = 1
while i <= n:
    prev = fact
    fact *= i
    print(f"In {i} iteration factorial is {prev} X {i} = {fact}")
    i += 1
print(f"Factorial of {n} using while loop: {fact}")