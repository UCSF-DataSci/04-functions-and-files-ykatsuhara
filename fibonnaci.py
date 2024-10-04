#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

import argparse

def generate_fibonacci(limit, file_name):
	fibonacci = [0,1]
	while True:
		updated_fibonacci = fibonacci[-1] + fibonacci[-2] # Generate new fibonacci number
		if updated_fibonacci >= limit:  # Stop generating number when the new fibonacci number is larger than the limit.
			break
		fibonacci.append(updated_fibonacci)

	try:
		with open(file_name, 'w') as file:
			for number in fibonacci:
				file.write(f'{number}\n')
	except IOError as e:
		print(f"Writing Error")
		
	return fibonacci



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Generate fibonacci number and save as a file")
    parser.add_argument('limit', type=int, help='Maximum')
    parser.add_argument('file_name', type=str, help='Name of File')
    
    args = parser.parse_args()

    fibonacci = generate_fibonacci(args.limit, args.file_name)
    print(fibonacci)