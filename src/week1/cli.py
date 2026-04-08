import sys

from src.week1.analyzer import count_words, top_n_words, word_stats
from src.week1.file_io import read_lines

"""command line tool that reads one or more text files,
analyzes word frequencies, and writes summary report.
Culmination project for week 1"""


def main():
    # get file name from terminal
    if len(sys.argv) != 2:
        print("Usage: python -m src.week1.cli <filename>")
        sys.exit(1)
    file_name = sys.argv[1]

    # check if file is empty & return error message
    lines = read_lines(file_name)
    if not lines:
        print(f"Error: File: {file_name} not found or is empty")
        sys.exit(1)

    # read file w/ imported function & join into a string
    file_as_str = " ".join(lines)

    # analyze the file & print results
    results = count_words(file_as_str)
    print(f"Word count: {sum(results.values())}")
    print(f"Top 5 words: {top_n_words(results, 5)}")
    print(f"Word stats: {word_stats(results)}")


if __name__ == "__main__":
    main()
