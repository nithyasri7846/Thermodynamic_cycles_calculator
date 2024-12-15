def calculate_otto():
    """Calculate the efficiency of the Otto cycle."""
    try:
        cr = float(input("ENTER THE COMPRESSION RATIO VALUE: "))
        R = 1.4  # Specific heat ratio
        otto = 1 - (1 / (pow(cr, R - 1)))
        efficiency = otto * 100
        print("THE EFFICIENCY OF THE OTTO CYCLE IS -----> ", round(efficiency, 2), "%")
    except ValueError:
        print("Invalid input! Please enter a valid numeric value.")


def calculate_diesel():
    """Calculate the efficiency of the Diesel cycle."""
    try:
        cr = float(input("ENTER THE COMPRESSION RATIO VALUE: "))
        cor = float(input("ENTER THE CUTOFF RATIO VALUE: "))
        R = 1.4  # Specific heat ratio
        a = 1 / (pow(cr, R - 1))
        b = (pow(cor, R) - 1) / (cor - 1)
        diesel = 1 - (a * b)
        efficiency = diesel * 100
        print("THE EFFICIENCY OF THE DIESEL CYCLE IS -----> ", round(efficiency, 2), "%")
    except ValueError:
        print("Invalid input! Please enter valid numeric values.")


def calculate_brayton():
    """Calculate the efficiency of the Brayton cycle."""
    try:
        rp = float(input("ENTER THE PRESSURE RATIO VALUE: "))
        R = 1.4  # Specific heat ratio
        a = (R - 1) / R
        brayton = 1 - (1 / pow(rp, a))
        efficiency = brayton * 100
        print("THE EFFICIENCY OF THE BRAYTON CYCLE IS -----> ", round(efficiency, 2), "%")
    except ValueError:
        print("Invalid input! Please enter a valid numeric value.")


def calculate_dual():
    """Calculate the efficiency of the Dual cycle."""
    try:
        cr = float(input("ENTER THE COMPRESSION RATIO VALUE: "))
        cor = float(input("ENTER THE CUTOFF RATIO VALUE: "))
        pr = float(input("ENTER THE PRESSURE RATIO VALUE: "))
        R = 1.4  # Specific heat ratio
        a = (pr * pow(cor, R)) - 1
        b = pr * R * (cor - 1)
        c = (pr - 1) + b
        d = pow(cr, R - 1) * c
        dual = 1 - (a / d)
        efficiency = dual * 100
        print("THE EFFICIENCY OF THE DUAL CYCLE IS -----> ", round(efficiency, 2), "%")
    except ValueError:
        print("Invalid input! Please enter valid numeric values.")


def display_menu():
    """Display the cycle options menu."""
    print("\n- - - - - - - - ->> EFFICIENCY OF THE CYCLE << - - - - - - - - -")
    print("- " * 30)
    print("Choose a cycle to calculate its efficiency:")
    print("1. Otto Cycle")
    print("2. Diesel Cycle")
    print("3. Brayton Cycle")
    print("4. Dual Cycle")
    print("5. Exit")
    print("- " * 30)


def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = input("\nENTER YOUR CHOICE (1-5): ").strip()
        if choice == "1":
            calculate_otto()
        elif choice == "2":
            calculate_diesel()
        elif choice == "3":
            calculate_brayton()
        elif choice == "4":
            calculate_dual()
        elif choice == "5":
            print("\nExiting the program. Thank you!")
            break
        else:
            print("\nInvalid choice! Please select a valid option.")
        print("\n", "- " * 30)


# Run the program
if __name__ == "__main__":
    main()

