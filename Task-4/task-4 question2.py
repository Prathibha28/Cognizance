"""q2----Write a program to accept a string from the user and display characters,
that are present at an even index number."""
user_str = input("enter the string")
even_char_str = ""
for i in range(len(user_str)):
    if i % 2 == 0:
        even_char_str += user_str[i]
print(f"Even characters: {even_char_str}")
