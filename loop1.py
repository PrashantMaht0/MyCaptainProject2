#Program to display the Fibonacci sequence 

n1 = int(input("enter the limit "))


n2, n3 = 0, 1
count = 0


print("Fibonacci sequence:")
while count < n1:
       print(n2)
       nth = n2 + n3
       n2 = n3
       n3 = nth
       count += 1
