# Prompt the user to enter any number
number = int(input("Enter a number to see its multiplication table: "))

# Print the multiplication table using a for loop. Here it loops through 1 to 12 for the input number.
print(f"Multiplication Table for {number}:")
for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")
