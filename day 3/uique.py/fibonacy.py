nterms = int(input("Enter the number of terms: "))


n1, n2 = 0, 1
count = 0


if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   
   print(nterms)
   print(n1)
else:
   print("the Fibonacci sequence of given number is :")
   while count < nterms:
       print(n1)
       nth = n1 + n2
    
       n1 = n2
       n2 = nth
       count += 1