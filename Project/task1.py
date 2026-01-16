# ==========================================
# TASK 1: BECKETT PIZZA PLAZA (4-FOR-3 OFFER)
# ==========================================

def calculate_pizza_order():
    print("Beckett Pizza Plaza 4-for-3 Offer")
    print("=================================")

    # List to store pizza prices
    pizza_prices = []

    # Get 4 valid pizza prices from the user
    for i in range(1, 5):
        while True:
            try:
                price = float(input(f"Enter Price of Pizza #{i}: "))
                if price <= 0:
                    print("Please enter a valid price!")  
                else:
                    pizza_prices.append(price)
                    break 
            except ValueError:
                print("Please enter a valid price!")  

    # Calculate total price and apply 
    total_price = sum(pizza_prices)
    cheapest_price = min(pizza_prices)
    order_total = total_price - cheapest_price

    # Calculate discount percentage
    if total_price > 0:
        discount = round((cheapest_price / total_price) * 100)
    else:
        discount = 0

    # Display the final result with formatted output
    print(f"Order Total is £{order_total:.2f}, a fabulous discount of {discount}%!")

if __name__ == "__main__":
    calculate_pizza_order()