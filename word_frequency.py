
import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]




def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    print (f"Your file is: {file}")
    with open(file) as open_file:
        read_file = open_file.read()
    new_read = read_file.translate(str.maketrans('','', string.punctuation)).lower()
    make_string = str.strip(new_read)
    split_string = str.split(make_string)
    remove_stop = [word for word in split_string if word not in STOP_WORDS]
    for sorta in sorted(set(remove_stop)):
        print(f"{sorta:>15} | {remove_stop.count(sorta)} {'*' * remove_stop.count(sorta)}")


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
