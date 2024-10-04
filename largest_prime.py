#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

import argparse
from fibonnaci import generate_fibonacci

# Check if the number is prime
def largest_prime_number(fibonacci):
    def check_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Create the list of prime number of fibonacci 
    prime_fibonacci_numbers = [num for num in fibonacci if check_prime(num)]
    
    # Reture Max of the prime number in fibonacci
    if prime_fibonacci_numbers:
        return max(prime_fibonacci_numbers)
    else:
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the largest prime Fibonacci number less than a given limit.")
    parser.add_argument('limit', type=int, help='The upper limit for Fibonacci numbers')
    parser.add_argument('file_name', type=str, help='The file to write Fibonacci numbers to')

    args = parser.parse_args()

    # Generte fibonacci numbers and save as a text file.
    fibonacci = generate_fibonacci(args.limit, args.file_name)
    
    # Identify the larget prime number
    largest_prime = largest_prime_number(fibonacci)

    if largest_prime is not None:
        print(f"The largest prime Fibonacci number is: {largest_prime}")
    else:
        print(f"No prime Fibonacci numbers found.")

