 API Documentation

This document provides an overview of the functions available in the `stats.py` module.

## `get_num_words(path)`

Calculates the total number of words in a given text file.

### Parameters

*   `path` (str): The path to the text file.

### Returns

*   `str`: A string indicating the total number of words found. Example: `"Found 12345 total words"`

### Example Usage

```python
from stats import get_num_words

word_count_str = get_num_words("books/frankenstein.txt")
print(word_count_str)
```

## `get_char_count(path)`

Calculates the frequency of each alphabetic character in a given text file. The analysis is case-insensitive and ignores non-alphabetic characters.

### Parameters

*   `path` (str): The path to the text file.

### Returns

*   `dict`: A dictionary where keys are lowercase alphabetic characters and values are their frequencies. The dictionary is sorted in descending order of frequency.

### Example Usage

```python
from stats import get_char_count

char_frequencies = get_char_count("books/prideandprejudice.txt")
for char, count in char_frequencies.items():
    print(f"{char}: {count}")
```