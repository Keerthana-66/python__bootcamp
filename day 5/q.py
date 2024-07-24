# print number pyramid

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

# print rhombus
num = int(input("Enter the number:"))
for i in range(0, num):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(0, num):
        print("*", end="")
    print()