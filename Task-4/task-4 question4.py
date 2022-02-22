"""q4----Write a program to check if the given number is a palindrome number."""

given_number = int(input("enter a number"))
reverse_number=0
temp = given_number
if given_number<=0:
    print(False)
else:
    while given_number>=1:
        reminder = given_number%10
        reverse_number = (reverse_number*10)+reminder
        given_number = given_number//10

if temp == reverse_number:
    print(True)
else:
    print(False)
