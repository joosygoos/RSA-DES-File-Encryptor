
import random


#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
def get_d(e, z):
    d=0
    def extended_gca(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gca(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    gcd, x, y = extended_gca(e, z)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    else:
        return x % z

def is_prime (num):
    if num > 1: 
      
        # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
               break
           else: 
               return True 
  
    else: 
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    e=0
    n=0
    d=0
    n = p * q
    z = (p - 1) * (q - 1)
    e = random.randrange(2, z)
    while gcd(e, z) != 1:
        e = random.randrange(2, z)
    d = get_d(e, z)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    cipher=0;
    e, n = pk
    ascii_value = ord(plaintext)
    encrypted_value = pow(ascii_value, e, n)
    return encrypted_value

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext
    plain='a'
    d, n = pk
    decrypted_value = pow(ciphertext, d, n)

    return chr(decrypted_value)

