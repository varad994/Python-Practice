
# Program to count the number of vowels in a string
string = input("Enter a string: ").lower()
vowels = "aeiou"
count = sum(1 for char in string if char in vowels)
print(f"The number of vowels in the string is: {count}")
