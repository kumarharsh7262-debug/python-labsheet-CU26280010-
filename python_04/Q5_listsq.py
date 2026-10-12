# list of squares of numbers from 1 to n

n = int(input("Enter n: "))
squares = []

for i in range(1, n + 1):
    squares.append(i ** 2)

print("Squares =", squares)