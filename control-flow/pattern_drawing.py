# pattern_drawing.py

size = int(input("Enter the size of the pattern: "))

row = 0  # Start row counter

while row < size:
    for col in range(size):
        print("*", end="")  # Print asterisk without a new line
    print()  # Move to next line after each row
    row += 1  # Go to next row
