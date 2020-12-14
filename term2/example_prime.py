prime = int(input("please enter number : "))
  

if prime > 1: 
      

 

   for i in range(2, prime//2): 
         

         
       if (prime % i) == 0: 

           print(prime, "is not a prime number") 

           break

   else: 

       print(prime, "is a prime number") 
  

else: 

   print(prime, "is not a prime number")