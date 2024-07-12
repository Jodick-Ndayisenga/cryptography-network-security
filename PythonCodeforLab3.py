import random
import math

class RSA:
    def __init__(self, bit_length=1024):
        self.bit_length = bit_length
        self.e = 65537  # Commonly used prime exponent

    def is_prime(self, num):
        """Check if a number is prime."""
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def generate_prime(self):
        """Generate a random prime number of specified bit length."""
        while True:
            num = random.getrandbits(self.bit_length)
            num |= (1 << self.bit_length - 1) | 1  # Ensure it's of bit_length and odd
            if self.is_prime(num):
                return num

    def gcd(self, a, b):
        """Compute the Greatest Common Divisor of a and b."""
        while b != 0:
            a, b = b, a % b
        return a

    def mod_inverse(self, a, m):
        """Compute the modular multiplicative inverse of a under modulo m."""
        m0, x0, x1 = m, 0, 1
        if m == 1:
            return 0
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1

    def generate_keys(self):
        """Generate RSA public and private keys."""
        p = self.generate_prime()
        q = self.generate_prime()
        while p == q:  # Ensure p and q are different
            q = self.generate_prime()

        n = p * q
        phi_n = (p - 1) * (q - 1)

        # Ensure that e and phi_n are coprime
        while self.gcd(self.e, phi_n) != 1:
            self.e = random.randrange(2, phi_n)

        d = self.mod_inverse(self.e, phi_n)

        # Public key: (e, n), Private key: (d, n)
        return (self.e, n), (d, n)

    def encrypt(self, plaintext, public_key):
        """Encrypt a plaintext message using the public key."""
        e, n = public_key
        ciphertext = [pow(ord(char), e, n) for char in plaintext]
        return ciphertext

    def decrypt(self, ciphertext, private_key):
        """Decrypt a ciphertext message using the private key."""
        d, n = private_key
        plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
        return plaintext

# Example usage:
if __name__ == "__main__":
    rsa = RSA(bit_length=512)  # Using 512 bits for demonstration purposes

    public_key, private_key = rsa.generate_keys()

    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    message = "Hello, RSA!"
    print(f"Original Message: {message}")

    encrypted_message = rsa.encrypt(message, public_key)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = rsa.decrypt(encrypted_message, private_key)
    print(f"Decrypted Message: {decrypted_message}")
