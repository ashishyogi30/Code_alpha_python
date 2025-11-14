import csv

stock_prices = {
    "APPLE": 180,
    "MANGO": 250,
    "ORANGE": 140,
    "GRAPES": 330,
    "BANANA": 120
}

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks and their prices:")
for stock, price in stock_prices.items():
    print(f"{stock.title()}: ${price}")

portfolio = {}

num_stocks = int(input("\nHow many different fruits do you own? "))

for i in range(num_stocks):
    name = input(f"\nEnter fruit name #{i+1} (Apple, Mango, Orange, Grapes, Banana): ").strip().upper()
    
    if name not in stock_prices:
        print("❌ Sorry, this fruit is not in our list. Try again.")
        continue

    qty = int(input("Enter quantity (number of fruits): "))
    portfolio[name] = qty
    
total_value = 0
print("\nYour Portfolio Summary:")
print("------------------------")
for name, qty in portfolio.items():
    price = stock_prices[name]
    value = qty * price
    total_value += value
    print(f"{name.title()}: {qty} × ${price} = ${value}")

print("------------------------")
print("Total Investment Value: $", total_value)

save = input("\nDo you want to save your portfolio to a file? (yes/no): ").lower()

if save == "yes":
    file_type = input("Save as .txt or .csv? Enter 'txt' or 'csv': ").lower()

    if file_type == "txt":
        with open("portfolio.txt", "w") as file:
            file.write("Your Portfolio Summary:\n")
            file.write("------------------------\n")
            for name, qty in portfolio.items():
                price = stock_prices[name]
                value = qty * price
                file.write(f"{name.title()}: {qty} × ${price} = ${value}\n")
            file.write("------------------------\n")
            file.write(f"Total Investment Value: ${total_value}\n")
        print("Portfolio saved to 'portfolio.txt' successfully!")

    elif file_type == "csv":
        with open("portfolio.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Fruit Name", "Quantity", "Price", "Total Value"])
            for name, qty in portfolio.items():
                price = stock_prices[name]
                value = qty * price
                writer.writerow([name.title(), qty, price, value])
            writer.writerow([])
            writer.writerow(["Total Investment Value", "", "", total_value])
        print("Portfolio saved to 'portfolio.csv' successfully!")

    else:
        print("Invalid file type. File not saved.")

print("\nThank you for using the Stock Portfolio Tracker!")
