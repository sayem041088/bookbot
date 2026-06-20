# BookBot

## Project Description

BookBot is a Python project designed to analyze a corpus of books. Currently, it processes text files to perform basic statistical analysis, such as word counting. The project aims to provide insights into large textual datasets and is planned for future enhancements to handle more extensive data with advanced tools.

## Features

*   **Word Count:** Calculates the total number of words in a given book (available via `stats.py`).
*   **Character Frequency:** Determines the frequency of each character in the text (used by `main.py`).
*   **Book Processing:** Reads and processes text files from the `books/` directory.

## API Documentation

For detailed information on the available functions and how to use them, please refer to the [API Documentation](docs/api.md).

## How to Run

To run BookBot, ensure you have Python installed.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/bookbot.git
    cd bookbot
    ```

2.  **Run the main script for character frequency analysis:**
    ```bash
    python main.py books/frankenstein.txt
    ```
    This will process the specified book and print the character frequency analysis to the console. Replace `books/frankenstein.txt` with the path to the book you wish to analyze.

## Technologies Used

*   Python 3

## Future Enhancements

*   Integration with **PySpark** for scalable data processing.
*   Implementation of **Apache Airflow** pipelines for workflow automation.
*   Extend `main.py` to include word count analysis as an option.

## Contributing

We welcome contributions to BookBot! Please see the [CONTRIBUTING guide](CONTRIBUTING.md) for details on how to contribute.
