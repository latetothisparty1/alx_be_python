
# pattern_drawing.py

# Prompt the user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the rows
row = 0

# While loop to iterate through each row
while row < size:
    # For loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")  # Print asterisk without moving to a new line
    print()  # Move to the next line after printing a row
    row += 1  # Increment the row counter
