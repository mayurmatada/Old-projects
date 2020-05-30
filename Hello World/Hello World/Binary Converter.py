Binary = input("Enter the Binary number you would like to convert to Decimal\n")
length = len(Binary)
print (Binary)
print (length)
Base = 0
Decimal = '00000000'


for i in range(length, 0, -1):
    print ("hello1\n")
    if(Binary[i-1] == 1):
        print("hello2\n")
        Decimal[length - i] = 2**Base    
    else:
        Decimal[length-i] = '0'
        print("hello3\n")
    Base = Base+1
print(Decimal)
Total = 0

for j in range(0, length):
    Total = Total + Decimal[j]

print("/n")
print(Total)
    
