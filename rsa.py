#Sydney Rudny
#May 2021
#This program runs a basic encryption and decryption using the RSA algorithm
#on a smaller scale due to computational complexity. (Encrypt small messages, 2-3
# characters at a time and use small primes for the key)
#Changes: RSA revised from Number Theory
#Original Authors: Sydney Rudny, Julia Krull, Nawaj KC

#Runs the Extended Euclidan Algorithm
def euclidan(a,b):
    numList=[]
    remainder=a%b
    while remainder!=0:
        numList.append(a//b)
        a=b
        b=remainder
        remainder=a%b
    coeff1=-1*numList[-1]
    coeff2=1
    length=len(numList)
    for i in range(length-1):
        replace=coeff1
        coeff1=coeff2+(coeff1*numList[length-2-i]*-1)
        coeff2=replace
    return coeff1,coeff2


#Inputs are the public keys
#Excepts messages/data in numeric form
#Due to limited computational resources keep messages to 1-3 charcters
def encryption(n,e):
    print('What message would you like to encrypt?')
    message=input()
    m=(int(message)**e)%n
    return m

#Modular function created for decryption 
def mod(number,exponent,mo):
    total=1
    while True:
        if exponent<5:
            total=(total*(number**exponent)%mo)
            break
        else:
            total=(total*(number**5)%mo)
        exponent-=5
    return total  

#Decryption method takes private key as input and asks for numeric encrypted message
def decryption(p,q,e):
    n=p*q
    print('What is your encoded message (as numbers) ?')
    m=input()
    d=euclidan((p-1)*(q-1),e)[0]
    
    answer=mod(int(m),d,n)
    return answer