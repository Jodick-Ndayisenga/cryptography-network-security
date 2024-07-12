"""This is Lab1 for Roy Tanga, Summer Semester 2024 Cryptography & Network Security (APT3090A)"""
import random

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

# Example usage:
if __name__ == "__main__":
    # Define the range for prime number generation
    range_start = 100
    range_end = 200

    key_gen = KeyGeneration(range_start, range_end)
    p, q = key_gen.generate_keys()

    print(f"Generated prime numbers:\np = {p}\nq = {q}")
