# ---------------------------------------------
# CodeAlpha - Stock Portfolio Tracker
# Author : Thirisha J
# ---------------------------------------------

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190,
    "META": 510,
    "NFLX": 650,
    "NVDA": 130,
    "IBM": 190,
    "ORCL": 145
}

portfolio = {}

print("=" * 55)
print("         STOCK PORTFOLIO TRACKER")
print("=" * 55)

print("\nAvailable Stocks")
print("-" * 55)

for stock, price in stocks.items():
    print(f"{stock:<10} : ${price}")

print("-" * 55)

while True:

    stock = input("\nEnter Stock Name (or 'done'): ").upper()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("❌ Invalid Stock Name! Please try again.")
        continue

    while True:
        try:
            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("❌ Quantity must be greater than 0.")
            else:
                break

        except ValueError:
            print("❌ Please enter numbers only.")

    # Add quantity if stock already exists
    portfolio[stock] = portfolio.get(stock, 0) + quantity


# ---------------- Portfolio Summary ----------------

print("\n")
print("=" * 55)
print("             PORTFOLIO SUMMARY")
print("=" * 55)

grand_total = 0

file = open("portfolio.txt", "w")

file.write("STOCK PORTFOLIO SUMMARY\n")
file.write("=" * 55 + "\n")

print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Total'}")
print("-" * 55)

file.write(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Total'}\n")
file.write("-" * 55 + "\n")

for stock, quantity in portfolio.items():

    price = stocks[stock]
    total = price * quantity
    grand_total += total

    print(f"{stock:<10}{quantity:<12}${price:<11}${total}")

    file.write(f"{stock:<10}{quantity:<12}${price:<11}${total}\n")

print("-" * 55)
print(f"Total Investment : ${grand_total}")

file.write("-" * 55 + "\n")
file.write(f"Total Investment : ${grand_total}\n")

file.close()

print("\n✅ Portfolio saved successfully in portfolio.txt")
print("🎉 Thank you for using Stock Portfolio Tracker!")
print("Have a Great Day! 😊")
