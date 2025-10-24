a = "text variable"
b = 42
c = 3.14

d = [1, "two", 3.0, True] # List
e = (1, "two", 3.0, True) # Tuple
f = { "key1": "value1", "key2": 2 } # Dictionary
g = {1, 2, 3, 4} # Set

################################################################

print("First constant:", True)
print("Second constant:", None)
print(f"Second constant: {Ellipsis}")

def f(a,b):
   return None

################################################################

a = [1, 2, 3, 4, 5]

b = max(a)
c = dir(a)
d = all(a)
print(f"""
      {b}
      {c}
      {d}
      """)

################################################################

for i in range(5):
    print(i)

list_a = [1, 2, 3, 4, 5, 6, 7, 8] 
for i in list_a :
    if i % 2 == 0 :
        print(f"Even number: {i}")
    else :
        print(f"Odd number: {i}")

i = 0
while i < 5 :
    print(f"i is: {i}")
    i += 1

################################################################

import random

A = random.randint(1, 100)
if A > 70:
   print("A is greater than 70")
else:
   print("A is 70 or less")


c_inpt = input("Bet on Heads or Tails:")
coin = random.choice(["Heads", "Tails"])
print(f"The coin landed on: {coin}")
if coin == c_inpt:
   print("You it right!")
else:
   print("You got it wrong or invalid input!")

################################################################

# try except finally example
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input.")
finally:
    print("Draniksigma.")

#################################################################

with open("testfile.md", "w") as file:
   file.write("# Loremipsum\n")
   file.write("## Dolorsitamet\n")
   file.write("### Consecteturadipiscingelit\n")
with open("testfile.md", "r") as file:
   content = file.read()
   print(content)

################################################################

to_lambda = lambda name,swaglvl: print(f"Their name is {name} and their swag level is {swaglvl}")
to_lambda("Dranik", 999)