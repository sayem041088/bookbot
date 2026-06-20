# BookBot

## Purpose
BookBot is a Python project that analyses text corpora of classic literature. It provides utilities for counting characters, words, and other textual statistics, serving as a foundation for larger data‑processing pipelines (e.g., Spark, Airflow).

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/bookbot.git
   cd bookbot
   ```
2. **Set up a virtual environment** (optional but recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *If `requirements.txt` does not exist, the project currently has no external dependencies beyond the Python standard library.*

## Usage Examples
### Counting characters in a book
```bash
python3 main.py books/frankenstein.txt
```
The script prints a frequency table of each character found in the specified text file.

### Using the library programmatically
```python
from stats import get_char_count, get_num_words

char_counts = get_char_count('books/mobydick.txt')
word_count = get_num_words('books/mobydick.txt')
print('Characters:', char_counts)
print('Total words:', word_count)
```

## Contribution Guidelines
1. **Fork the repository** and clone your fork.
2. **Create a new branch** for your feature or bug‑fix:
   ```bash
   git checkout -b my-feature
   ```
3. **Make your changes** and ensure the existing functionality still works.
4. **Write tests** (if applicable) and run them.
5. **Commit** your changes with clear messages.
6. **Push** to your fork and open a Pull Request against the `main` branch.

### Code Style
- Follow PEP 8 conventions.
- Use descriptive variable and function names.
- Include docstrings for all public functions and modules.

### Reporting Issues
Please open an issue on GitHub with a clear description, steps to reproduce, and any relevant logs or screenshots.
