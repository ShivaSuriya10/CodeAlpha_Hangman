# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 140,
    "MSFT": 330,
    "AMZN": 135
}

total_value = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_value += value
    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total_value)

# Save result in a text file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value = $" + str(total_value))

print("Result saved in portfolio.txt")
