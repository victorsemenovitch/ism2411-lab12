
# Reflection 1:
# Python makes it easier to automate data cleaning and repeat tasks.
# Excel is easier for viewing data and creating quick charts.
# Python is better for processing many files automatically.

# Reflection 2:
# A store could use append mode to track daily sales.
# It keeps older records and adds new ones without deleting anything.

import csv
from datetime import datetime

# Exercise 1 & 2: Read all rows
print("EXERCISE 2")
with open("data/sales.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Exercise 3: Skip header
print("\nEXERCISE 3")
with open("data/sales.csv", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# Exercise 4: Total revenue
print("\nEXERCISE 4")
revenue = 0

with open("data/sales.csv", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity
        revenue += total
        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${revenue:.2f}")

# Exercise 5: Cleaned CSV
print("\nEXERCISE 5")
original = 0
written = 0

with open("data/sales.csv", newline="") as infile, \
     open("data/cleaned.csv", "w", newline="") as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])

    for row in reader:
        original += 1
        total = float(row[1]) * int(row[2])

        if total > 100:
            writer.writerow([row[0], row[1], row[2], f"{total:.2f}"])
            written += 1

print(f"Written: {written} out of {original} rows")

# Exercise 6: DictReader
print("\nEXERCISE 6")
# csv.reader is good for simple files with fixed column positions.
# DictReader is better when you want to access data by column name.

dict_total = 0

with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total = float(row["price"]) * int(row["quantity"])
        dict_total += total
        print(f'{row["product"]}: ${total:.2f}')

print(f"DictReader total: ${dict_total:.2f}")

# Exercise 7: Sales summary
print("\nEXERCISE 7")
summary = {}

with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

# Exercise 8: Append log
print("\nEXERCISE 8")

with open("data/run_log.txt", "a") as file:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"{now} - Total Revenue: ${revenue:.2f}\n")

print("Log updated successfully!")
