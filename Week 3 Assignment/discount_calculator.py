# Discount Calculator Function
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Applies discount only if 20% or higher, otherwise returns original price.
    Args:
        price (float): Original price of the item
        discount_percent (float): Discount percentage to apply
    Returns:
        float: Final price after discount (if applicable)
    """
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent/100)
        return discounted_price
    else:
        return price

# Main program
def main():
    print("Welcome to the Discount Calculator!")
    print("----------------------------------")
    
    # Get user input with validation
    while True:
        try:
            original_price = float(input("Enter the original price of the item: $"))
            if original_price <= 0:
                print("Price must be greater than 0. Please try again.")
                continue
            
            discount_percent = float(input("Enter the discount percentage (0-100): "))
            if discount_percent < 0 or discount_percent > 100:
                print("Discount must be between 0 and 100. Please try again.")
                continue
            
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    
    # Calculate and display result
    final_price = calculate_discount(original_price, discount_percent)
    
    if discount_percent >= 20:
        print(f"\nApplying {discount_percent}% discount...")
        print(f"Original price: ${original_price:.2f}")
        print(f"Discounted price: ${final_price:.2f}")
        print(f"You saved: ${original_price - final_price:.2f}")
    else:
        print(f"\nDiscount too low ({discount_percent}%). No discount applied.")
        print(f"Final price: ${original_price:.2f}")

# Run the program
if __name__ == "__main__":
    main()