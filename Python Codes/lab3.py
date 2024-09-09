string = input("Please Enter a Number or string: ")
revString=string[::-1]
if string==revString:
    print(f"{string} is Palindrome")
else:
    print(f"{string} is not Palindrome")