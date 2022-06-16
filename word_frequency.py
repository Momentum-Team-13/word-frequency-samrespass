

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
        for stop in STOP_WORDS:
            string = read_file.replace(stop, '').lower()
            for puncs in STOP_PUNC:
                no_punc = string.replace(puncs, '')
    make_dic = str.split(no_punc)
    for lyrics in sorted(set(make_dic)):
        print("| |", lyrics, "|", make_dic.count(lyrics))


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
