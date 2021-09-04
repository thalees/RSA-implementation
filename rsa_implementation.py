
import random
import ast
import base64
max_prim_length = 1000000000000

def get_keys_from_file(
    private_keys_path = "private_keys.txt", 
    public_keys_path = "public_keys.txt"
):
    public_keys_file = open(public_keys_path, 'r')
    e = int(public_keys_file.readline())
    n = int(public_keys_file.readline())
    public_keys_file.close()

    private_keys_file = open(private_keys_path, 'r')
    d = int(private_keys_file.readline())
    n = int(private_keys_file.readline())
    private_keys_file.close()
    
    return ((e,n), (d,n))

def generate_key_pairs():
    p = _generateRandomPrim()
    q = _generateRandomPrim()

    n = _generate_RSA_modulus(p, q)

    phi = _calculate_eulers_totient_function(p, q)
    
    e = random.randint(1, phi)
    g = _gcd(e,phi)
    while g != 1:
        e = random.randint(1, phi)
        g = _gcd(e, phi)

    d = _egcd(e, phi)[1]
    
    d = d % phi
    if(d < 0):
        d += phi
        
    return ((e,n), (d,n))

def encrypt(message: str, public_key):
    key, n = public_key
    arr = [pow(ord(char), key, n) for char in message]

    return base64.b64encode(bytes(str(arr), 'ascii')).decode()

def dencrypt(message, private_key):
    try:
        key, n = private_key
        
        message_decoded = base64.b64decode(message).decode()
        arr = ast.literal_eval(message_decoded)

        message_dencrypted = ""
        text = [chr(pow(char, key, n)) for char in arr]
        
        return message_dencrypted.join(text)
    except TypeError as e:
        raise e
        
def save_keys(public_key, private_key):
    public_file = open('public_keys.txt', 'w')
    public_file.write(str(public_key[0]) + '\n')
    public_file.write(str(public_key[1]) + '\n')
    public_file.close()

    private_file = open('private_keys.txt', 'w')
    private_file.write(str(private_key[0]) + '\n')
    private_file.write(str(private_key[1]) + '\n')
    private_file.close()

def _is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def _generateRandomPrim():
    while(1):
        ranPrime = random.randint(0, max_prim_length)
        if _is_prime(ranPrime):
            return ranPrime

def _generate_RSA_modulus(p: int, q: int):
    '''selection of two prime numbers namely p and q, and then 
    calculating their product N'''

    return p * q

def _calculate_eulers_totient_function(p: int, q: int):
    '''counts the positive integers up to a given integer n that
    are relatively prime to n.'''
    return (p-1) * (q-1) 

def _gcd(a, b):
    '''
    calculates the gcd of two ints
    '''
    while b != 0:
        a, b = b, a % b
    return a
    
def _egcd(a, b):
    '''
    calculates the modular inverse from e and phi
    '''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = _egcd(b % a, a)
        return (g, x - (b // a) * y, y)
