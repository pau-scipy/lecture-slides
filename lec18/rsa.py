import sys
import random
import numpy as np

def make_primes(t):
    """Return a list of prime numbers between 2 and t.
    Use any method you like. One option is the Sieve of Erathosthenes."""
    return None

def choose_e(t):
    """Choose a random prime number e between 2 and t (using make_primes) such that e does not divide t. Return e."""
    return None

def get_primes():
    """Ask the user to enter two prime numbers, eg 7 and 17, from which to construct the keys"""
    print("enter prime p:")
    p = int(sys.stdin.readline())
    print("enter prime q:")
    q = int(sys.stdin.readline())
    return (p, q)


def egcd(a, b):
    """returns a triple (g, x, y), such that ax + by = g = gcd(a, b)
    https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm"""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modular_inverse(e, m):
    """Find the modular inverse of e, modulo m, using egcd"""
    g, x, y = egcd(e, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def calc_d(e, t):
    """Calculate d, the modular inverse of e modulo t. Return d."""
    return None



def get_message():
    """Ask the user for a message to encrypt"""
    print("input the message")
    message = sys.stdin.readline().strip()
    return message


def encrypt(message,n,e):
    """Encrypt the message with public key n and e"""
    numeric_codes = [ord(c) for c in message]
    return [pow(m,e,n) for m in numeric_codes]


def decrypt(encrypted,n,d):
    """Decrypt the message with private key d, and also n"""
    return [chr(pow(enc,d,n)) for enc in encrypted]


def euler_totient(n, p, q):
    """Calculate Euler's totient of n (how many numbers are relatively prime to n).
    Hint, we know that n is a product of the two primes p and q.
    See http://mathworld.wolfram.com/TotientFunction.html"""
    return None


if __name__ == "__main__":
    (p, q) = get_primes()
    message = get_message()
    n = p * q
    t = euler_totient(n, p, q)
    print("t is:" + str(t))
    e = choose_e(t)
    print("e is:" + str(e))
    d = calc_d(e,t)
    print("d is:" + str(d))
    enc = encrypt(message, n, e)
    print(enc)
    resp = decrypt(enc, n, d)
    print(resp)

    

