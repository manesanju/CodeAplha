import csv
from datetime import datetime

# Hardcoded stock prices dictionary
STOCK_PRICES = {
    "AAPL": 180.50,
    "TSLA": 250.75,
    "GOOGL": 135.25,
    "MSFT": 415.80,
    "AMZN": 145.60,
    "META": 485.20,
    "NFLX": 445.90,
    "NVDA": 875.30,
    "SPY": 425.15,
    "QQQ": 385.40
}

def display_available_stocks():
    """Display all available stocks and their prices"""
    print("\n" + "="*50)
    print("AVAILABLE STOCKS AND CURRENT PRICES")
    print("="*50)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<8} ${price:>8.2f}")
    print("="*50)

def get_portfolio_input():
    """Get portfolio input from user"""
    portfolio = {}
    
    print("\nEnter your stock portfolio (press Enter with empty stock name to finish):")
    
    while True:
        stock_name = input("\nStock symbol: ").strip().upper()
        
        if not stock_name:
            break
            
        if stock_name not in STOCK_PRICES:
            print(f"Error: {stock_name} not found in available stocks.")
            continue
        
        try:
            quantity = float(input(f"Quantity of {stock_name}: "))
            if quantity <= 0:
                print("Quantity must be positive!")
                continue
                
            portfolio[stock_name] = quantity
            print(f"Added: {quantity} shares of {stock_name}")
            
        except ValueError:
            print("Invalid quantity! Please enter a number.")
    
    return portfolio

def calculate_portfolio_value(portfolio):
    """Calculate total portfolio value and individual stock values"""
    stock_values = {}
    total_value = 0
    
    for stock, quantity in portfolio.items():
        stock_price = STOCK_PRICES[stock]
        stock_value = quantity * stock_price
        stock_values[stock] = {
            'quantity': quantity,
            'price': stock_price,
            'total_value': stock_value
        }
        total_value += stock_value
    
    return stock_values, total_value

def display_portfolio_summary(stock_values, total_value):
    """Display portfolio summary"""
    print("\n" + "="*70)
    print("PORTFOLIO SUMMARY")
    print("="*70)
    print(f"{'Stock':<8} {'Quantity':<10} {'Price':<12} {'Total Value':<15}")
    print("-"*70)
    
    for stock, data in stock_values.items():
        print(f"{stock:<8} {data['quantity']:<10.2f} ${data['price']:<11.2f} ${data['total_value']:<14.2f}")
    
    print("-"*70)
    print(f"{'TOTAL PORTFOLIO VALUE:':<45} ${total_value:<14.2f}")
    print("="*70)

def save_to_file(stock_values, total_value, file_format):
    """Save portfolio to file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if file_format.lower() == 'csv':
        filename = f"portfolio_{timestamp}.csv"
        
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Stock Symbol', 'Quantity', 'Price per Share', 'Total Value'])
            
            for stock, data in stock_values.items():
                writer.writerow([stock, data['quantity'], data['price'], data['total_value']])
            
            writer.writerow(['', '', 'TOTAL PORTFOLIO:', total_value])
    
    else:  # txt format
        filename = f"portfolio_{timestamp}.txt"
        
        with open(filename, 'w') as file:
            file.write("STOCK PORTFOLIO SUMMARY\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("="*50 + "\n\n")
            
            file.write(f"{'Stock':<10} {'Quantity':<12} {'Price':<12} {'Total Value':<15}\n")
            file.write("-"*50 + "\n")
            
            for stock, data in stock_values.items():
                file.write(f"{stock:<10} {data['quantity']:<12.2f} ${data['price']:<11.2f} ${data['total_value']:<14.2f}\n")
            
            file.write("-"*50 + "\n")
            file.write(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}\n")
    
    print(f"\nPortfolio saved to: {filename}")

def main():
    """Main program function"""
    print("🏦 STOCK PORTFOLIO TRACKER 🏦")
    print("Track your investments with ease!")
    
    # Display available stocks
    display_available_stocks()
    
    # Get user portfolio input
    portfolio = get_portfolio_input()
    
    if not portfolio:
        print("\nNo stocks entered. Goodbye!")
        return
    
    # Calculate portfolio values
    stock_values, total_value = calculate_portfolio_value(portfolio)
    
    # Display summary
    display_portfolio_summary(stock_values, total_value)
    
    # Ask if user wants to save to file
    save_choice = input("\nWould you like to save this portfolio summary? (y/n): ").strip().lower()
    
    if save_choice == 'y' or save_choice == 'yes':
        format_choice = input("Choose format (txt/csv): ").strip().lower()
        
        if format_choice in ['txt', 'csv']:
            try:
                save_to_file(stock_values, total_value, format_choice)
            except Exception as e:
                print(f"Error saving file: {e}")
        else:
            print("Invalid format! Defaulting to txt format.")
            save_to_file(stock_values, total_value, 'txt')
    
    print("\nThank you for using Stock Portfolio Tracker! 📈")

if __name__ == "__main__":
    main()