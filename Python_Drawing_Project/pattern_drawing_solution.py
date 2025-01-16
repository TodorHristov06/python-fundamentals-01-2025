# Step 1: Display a menu to the user
print("🌟 Welcome to the Python Pattern Drawing Program!")
print("Choose a pattern type:")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond")
print("4. Left-angled Triangle")
print("5. Hollow Square")
print("6. Pyramid")
print("7. Reverse Pyramid")
print("8. Rectangle with Hollow Center")

# Step 2: Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))

# Step 3: Get dimensions based on choice
if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
    rows = int(input("Enter the number of rows: "))
elif choice in [2, 5, 8]:  # Patterns that need size
    size = int(input("Enter the size of the square/rectangle: "))

# Step 4: Generate the selected pattern
if choice == 1:  # Right-angled Triangle
    for row in range(rows):
        for col in range(row + 1):
            print("*", end="")

elif choice == 2:  # Square with Hollow Center
    for row in range(size):
        for col in range(size):
            if row == 0 or row == size - 1 or col == 0 or col == size - 1:
                print("*", end="")
            else:
                print(" ", end="")  
        print() 

elif choice == 3:  # Diamond
    for i in range(rows):  
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))

    for i in range(rows - 2, -1, -1):  
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))

elif choice == 4:  # Left-angled Triangle
    for i in range(rows, 0, -1):  
        print("*" * i)

elif choice == 5:  # Hollow Square
    for i in range(size):
        if i == 0 or i == size - 1:  
            print("*" * size)
        else: 
            print("*" + " " * (size - 2) + "*")

elif choice == 6:  # Pyramid
    for row in range(1, rows + 1):
        spaces = rows - row
        stars = 2 * row - 1
        
        print(" " * spaces + "*" * stars)

elif choice == 7:  # Reverse Pyramid
   for row in range(rows, 0, -1):
        spaces = rows - row
        stars = 2 * row - 1
        
        print(" " * spaces + "*" * stars)

elif choice == 8:  # Rectangle with Hollow Center
    # TODO: Handle separate width and height inputs for rectangle
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    print("⚠️ This pattern is not implemented yet. Please choose another.")

else:
    print("❌ Invalid choice! Please restart the program.")

# Step 5: Optional - Allow the user to restart or exit