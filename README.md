# BookBot

## Project Description

BookBot is a Python project designed to analyze a corpus of books. Currently, it processes text files to perform basic statistical analysis, such as word counting. The project aims to provide insights into large textual datasets and is planned for future enhancements to handle more extensive data with advanced tools.

## Features

*   **Character Frequency:** Determines the frequency of each alphabetic character in the text, case-insensitively.
*   **Word Count:** Calculates the total number of words in a given book (accessible via the `stats.py` module).
*   **Book Processing:** Reads and processes text files from the `books/` directory.

## How to Run

To run BookBot, ensure you have Python installed.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/bookbot.git
    cd bookbot
    ```

2.  **Run the main script with a book path:**
    ```bash
    python3 main.py <path_to_book>
    ```
    For example, to analyze `frankenstein.txt`:
    ```bash
    python3 main.py books/frankenstein.txt
    ```
    This will process the specified book and print the character frequency analysis to the console.

## Technologies Used

*   Python 3

## Future Enhancements

*   Integration with **PySpark** for scalable data processing.
*   Implementation of **Apache Airflow** pipelines for workflow automation.

## Contributing

We welcome contributions to BookBot! Please see the [CONTRIBUTING guide](CONTRIBUTING.md) for details on how to contribute.
