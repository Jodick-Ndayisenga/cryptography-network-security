import random
import math

class KeyGeneration:
    def __init__(self, range_start, range_end):
        self.range_start = range_start
        self.range_end = range_end
    
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
        """Generate a random prime number within the specified range."""
        while True:
            num = random.randint(self.range_start, self.range_end)
            if self.is_prime(num):
                return num

    def generate_keys(self):
        """Generate two prime numbers, p and q."""
        p = self.generate_prime()
        q = self.generate_prime()
        while p == q:  # Ensure p and q are different
            q = self.generate_prime()
        return p, q

    def euler_totient(self, n):
        """Compute Euler's Totient function for a given number n."""
        result = n
        p = 2
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n //= p
                result -= result // p
            p += 1
        if n > 1:
            result -= result // n
        return result

# Example usage:
if __name__ == "__main__":
    # Define the range for prime number generation
    range_start = 100
    range_end = 200

    key_gen = KeyGeneration(range_start, range_end)
    p, q = key_gen.generate_keys()

    phi_p = key_gen.euler_totient(p)
    phi_q = key_gen.euler_totient(q)

    print(f"Generated prime numbers:\np = {p}\nq = {q}")
    print(f"Euler's Totient function values:\nφ(p) = {phi_p}\nφ(q) = {phi_q}")
