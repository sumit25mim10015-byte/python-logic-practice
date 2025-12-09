# 1. Print numbers 1 to N using while loop

i = 0
n = 51
while n > i:
    print(i)
    i+=1

# 2. Print all odd numbers from 1 to 100

for i in range(1 , 101):
    if (i %2 !=0):
        print(i)

# 3. Print numbers divisible by 3 between 1 and 50

for i in range(1,50):
    if(i % 3 ==0):
        print(i)

# 4. sum of odd numbers from 1 to n 

n = int(input("enter a numbr:"))

sum = 0
for i in range(1 ,n+1):
    if (i % 2 != 0):
        sum = sum + i
print(sum)

# 5. product(multiplication) of digit of a number

number = int(input("enter a number:"))
product = 1

while number>0:
    digit = number % 10
    product = product * digit
    number = number // 10
print(product)

# 6. largest digit in a number

input = int(input("enter a numbr:"))
largest = 0

for i in range(1, input):
    digit = input % 10
    if digit > largest:
        largest = digit
    input = input //10
print(largest)
    
    # or (simple method to find largest digit in a number)

inp = (input("Enter a number:"))
largest1 = max(inp) 
print(largest1)

# 7. smallest number in a digit

num = int(input("Enter a number:"))
smallest = 9

while num > 0 :
    digit = num % 10
    if (smallest > digit):
        smallest = digit
    num = num//10
print(smallest)

# 8. Armstrong number

num2 = int(input("enter a number:"))
count_digits = len(str(num2))
total = 0
original_number = num2

while num2 > 0:
    digit = num2 % 10
    total = total + digit ** count_digits
    num2 = num2 // 10
if total == original_number:
 print("number is armstrong")
else:
    print("not armstrong")

