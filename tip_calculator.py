"""A simple tip calculator script"""


def calculate_tip(bill_amount, tip_percent):
    """Calculate the tip and total based on bill amount and tip percent."""
    tip = bill_amount * tip_percent / 100
    total = bill_amount + tip
    return tip, total


def main():
    try:
        bill_input = float(input("Enter bill amount: "))
        percent_input = float(input("Enter tip percentage: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    tip, total = calculate_tip(bill_input, percent_input)
    print(f"Tip: ${tip:.2f}")
    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
