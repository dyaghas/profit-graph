import matplotlib.pyplot as plt

print("Welcome to the profit calculator! Here you will be able to see graphically how much you gained/lost"
      " in a selected period of time\n")

xInput = input("How many values do you want to calculate? Example: how much did I profit "
               "each month this year, (12): ")

xInput = int(xInput)

# Revenue line
x1 = []
y1 = []

i = 0

while xInput > i:
    revenueValue = float((input(f"Revenue {i+1}: ")))
    y1.append(revenueValue)
    x1.append(i)
    i += 1

# Loss line
x2 = []
y2 = []

i = 0

while xInput > i:
    expensesValue = float((input(f"Expenses {i+1}: ")))
    y2.append(expensesValue)
    x2.append(i)
    i += 1

# Profit line
x3 = []
y3 = []

for i in x1:
    print(i)
    y3.append(y1[i-1] - y2[i-1])
    x3.append(i)

plt.xlabel("time")
plt.ylabel("Value")

plt.xlim(0, xInput-1)

plt.plot(x1, y1, color="green", label="Revenue")
plt.plot(x2, y2, color="red", label="Expenses")
plt.plot(x3, y3, color="blue", label="profit")

plt.legend()
plt.show()