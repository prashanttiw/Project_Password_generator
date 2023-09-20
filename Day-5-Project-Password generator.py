#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in range(1,nr_letters+1):
    pr_letters=random.choice(letters)
    print(pr_letters,end="")

for i in range(1,nr_symbols+1):
    pr_symbols=random.choice(symbols)
    print(pr_symbols,end="")

for i in range(1,nr_numbers+1):
    pr_numbers=random.choice(numbers)
    print(pr_numbers,end="")

print("\n")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
new_list=[]
for i in range(1,nr_letters+1):
    or_letters=random.choice(letters)
    new_list.append(or_letters)

for i in range(1, nr_symbols + 1):
        or_symbols = random.choice(symbols)
        new_list.append(or_symbols)

for i in range(1,nr_numbers+1):
    or_numbers=random.choice(numbers)
    new_list.append(or_numbers)

random.shuffle(new_list)

for i in new_list:
    print(i,end="")