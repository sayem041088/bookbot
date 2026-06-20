"""
main.py

This script serves as the entry point for the word counter application. It takes a path to a book file as a command-line argument,
calculates the character count of the book, and prints the counts for each character.
"""

import sys
from stats import get_num_words, get_char_count

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the path to the book from the command-line arguments
    path = sys.argv[1]

    # Calculate character counts
    counts = get_char_count(path)

    # Print character counts
    for char, count in counts.items():
        print(f"{char}: {count}")