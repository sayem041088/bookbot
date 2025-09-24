import sys
from stats import get_num_words,get_char_count
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    counts = get_char_count(path)
    for char, count in counts.items():
        print(f"{char}: {count}")