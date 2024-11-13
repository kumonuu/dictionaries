# string = input("Enter a string: ")
# vowels = {
#     "a": 0,
#     "e": 0,
#     "i": 0,
#     "o": 0,
#     "u": 0
# }

# for letter in string:
#     if letter in vowels:
#         vowels[letter] += 1

# print(vowels)

number = input("Enter a number: ")
is_panagram = True
count_is_zero = False
repeating_digits = False
digits = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0
}

for digit in number:
    if digit in digits:
        digits[digit] += 1
for count in digits.values():
    if count == 0:
        is_panagram = False
        count_is_zero = True
    if count > 1:
        is_panagram = False
        repeating_digits = True
    if is_panagram == False:
        break
if is_panagram == True:
    print("The number is a panagram")
    print(digits)
elif count_is_zero == True:
    print("The number is not a panagram because count of a digit is zero")
    print(digits)
elif repeating_digits == True:
    print("The number is not a panagram because there are repeating digits")
    print(digits)