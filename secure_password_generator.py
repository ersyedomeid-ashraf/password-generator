"""
PASSWORD GENERATOR - WORKFLOW

1- Import Required Module
- Import random module.

2- Create Character Lists
- Create letters list.
- Create numbers lists.
- Create symbols lists.

3- Display Welcome Message
- Print welcome message.

4- Input from User
- Enter number of letters.
- Enter number of numbers.
- Enter number of symbols.

5- Generate Password

Case 1 (Letters) :
- Randomly select letters.
- Add selected letters to password list.

Case 2 (Numbers) :
- Randomly select numbers.
- Add selected numbers to password list.

Case 3 (Symbols) :
- Randomly select symbols.
- Add selected symbols to password list.

6- Shuffle Password
- Shuffle the password list randomly.

7- Generate Final Password
- Join all characters into a single string.

8- Display Output
- Print the generated password.

9- End
-Exit the program.

"""

import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to Password Generator! ")

n_letters = int(input("How many letters you want in your password?\n"))
n_numbers = int(input("How many numbers you want in your password?\n"))
n_symbols = int(input("How manny symbols you want in your password?\n"))

password_list = []

for i in range(1, n_letters + 1):
    char = random.choice(letters)
    password_list += char

for i in range(1, n_numbers + 1):
    char = random.choice(numbers)
    password_list += char

for i in range(1, n_symbols + 1):
    char = random.choice(symbols)
    password_list += char

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list:
    password += char


print(password)
