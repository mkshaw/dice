"""

main.py

Input number of random numbers you want, and return that many.
"""
import argparse
import random

def main():

    # Define arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('number', help='number of dice you want to output.')

    args = parser.parse_args()

    # Generate and print random number
    number = int(args.number)
    i = 0

    while i < number:
        print(random.randint(1, 6))
        i += 1
    

if __name__ == '__main__':
    main()
