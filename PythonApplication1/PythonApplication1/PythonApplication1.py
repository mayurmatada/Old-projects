import array as arr
Binary = input("Please enter the Binary Code you want to convert: ")
Base = len(Binary)
Decimal = [0, 0, 0, 0, 0, 0, 0, 0]
Total = 0
n = 0
for i in Binary:
    if i == '1':
        Decimal[n] = 2**Base
    if i == '0':
        Decimal[n]
    Base = Base-1
    n = n+1
for j in range(0, len(Binary), 1):
    Total = Total+Decimal[j]
print(Total)



