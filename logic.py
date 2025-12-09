# 1.print 1 to 10 using for loop

for i in range(1 , 11):
    print(i)

# 2.print 10 to 1 using while loop

i=10
while -1< i:
    print(i)
    i-=1

# 3.even numbers from 1 to 50 using while loop


n= int(input("enter a num:"))
i=n
while i <= n:
    if(i % 2 ==0):
        print(i ,"is even")
    else:
        print(i , "is odd")
    i+=1

# 4.even number from 1 to 50 using for loop

n = int(input("Enter a number:"))

for i in range(n , n+1):
    if(n %2==0):
        print(n,"is even")
    else:
        print(n ,"is odd")


# 5.sum of first n natural numbers using for loop

a= int(input("Enter a number:"))
sum =0

for i in range(1 , a + 1):
    sum+=i
print(sum)

# 6.digit of a number


b = int(input("Enter number: "))

while b > 0:
    digit = b % 10
    print(digit)
    b = b //10
    print(sum)

# 7.sum of even numbers

a= int(input("Enter a number:"))
sum =0


for i in range(1 , a + 1):
    if(i % 2==0):
        sum+=i
print(sum)\

# 8.count digits of a number

c = int(input("Enter number: "))
sum1 = 0
while c > 0:
    c = c //10
    sum1 = sum1 + 1
    
print(sum1)

# 9.reverse a number using while loop

d = int(input("Enter a mumber: "))
reverse = 0

while d>0:
    digit = d % 10
    reverse = reverse*10 + digit
    d= d//10
    
print(reverse)

# 10.check if a number is palindrone

e = int(input("Enter a mumber: "))
reverse = 0
original = e

while e > 0:
    digit = e % 10
    reverse = reverse*10 + digit
    e = e //10
    
if (original == reverse):
    print("the number is palindrone")
else:
    print("not palindrone")


# 11.fibonacci series 

f = int(input("enter number of terms: "))
a1 = 0
b1 = 1

for i in range (f):
    print(a1, end=" ")
    c1 = a1 + b1
    a1 = b1
    b1 = c1


#   12. factorial of a number

h = int(input("Enter a number:"))
fact = 1
for i in range (1,h+1):
    fact = fact * i
print(fact)


# 13.multiplication  table of a number using for loop

n0 = int(input("Enter a number: "))

for i in range(1 , 11):
    print(f"{n0} X {i} = {n0 * i}")


# 14.multiplication table of a number using while loop

i = 1
n9 = int(input("Enter a number:"))

while i < 11:
    print(f"{n9} X {i} = {n9*i}")
    i+=1 

# 15. count vowels in a string

v = "aeiou"

inp = input("enter your sentance: ")
count = 0 

for ch in inp:
  if ch in v :
    count+=1
if count > 0 :
    print("number of strings", count)
else:
    print("no vowels find")