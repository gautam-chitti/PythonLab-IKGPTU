a=20
prime_no =[1]
count=0
for i in range (2,a,1):
    is_prime = True
    for j in range (2,i,1):
       b=i%j
       if( b==0):
           is_prime = False
           break
       
    if is_prime:
       prime_no.append(i)

print (prime_no)