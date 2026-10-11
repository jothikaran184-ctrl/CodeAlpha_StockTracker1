def stock_portfolio():
    # Hardcoded dictionary defining stock prices
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 400, "AMZN": 170}
    portfolio = {}
    
    print("=== Stock Portfolio Tracker ===")
    print("Available Stock Prices:", stock_prices)
    
    while True:
        stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock not found in price list. Please try again.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
        except ValueError:
            print("Please enter a valid integer for quantity.")
            continue
            
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        
    total_investment = 0
    print("\n--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_investment += value
        print(f"{stock}: {qty} shares @ ${price} each = ${value}")
        
    print(f"\nTotal Investment Value: ${total_investment}")
    
    # Optional file saving
    save = input("Do you want to save this result to a file? (y/n): ").lower()
    if save == 'y':
        filename = "portfolio_summary.txt"
        with open(filename, "w") as f:
            f.write("--- Portfolio Summary ---\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                f.write(f"{stock}: {qty} shares @ ${price} = ${price * qty}\n")
            f.write(f"\nTotal Investment Value: ${total_investment}\n")
        print(f"Summary successfully saved to {filename}")

if __name__ == "__main__":
    stock_portfolio()