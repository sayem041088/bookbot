def get_num_words(path: str) -> str:
    """
    Calculates the total number of words in a given text file.

    Args:
        path (str): The path to the text file.

    Returns:
        str: A string indicating the total number of words found.
    """
    word_count = 0
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            words=line.split()
            word_count += len(words)
        return f"Found {word_count} total words"
            
def get_char_count(path: str) -> dict:
    """
    Calculates the frequency of each alphabetic character in a given text file.
    Case-insensitive and ignores non-alphabetic characters.

    Args:
        path (str): The path to the text file.

    Returns:
        dict: A dictionary where keys are lowercase alphabetic characters
              and values are their frequencies, sorted in descending order
              of frequency.
    """
    char_counts = {}
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line.lower():   # lowercase to treat 'A' and 'a' the same
                if char.isalpha():      # count only letters
                    char_counts[char] = char_counts.get(char, 0) + 1
        sorted_char_counts = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
        return sorted_char_counts