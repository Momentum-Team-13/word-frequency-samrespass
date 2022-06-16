
import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

STOP_PUNC = [
    ',', '.',',','?',
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    print (f"Your file is: {file}")
    with open(file) as open_file:
        read_file = open_file.read()
    new_read = read_file.translate(str.maketrans('','', string.punctuation)).lower()
    new_read = str.strip(new_read)
    new_read = str.split(new_read)
    new_read = [word for word in new_read if word not in STOP_WORDS]
    for sorta in sorted(set(new_read)):
        print("| |", sorta, "|", new_read.count(sorta))


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
