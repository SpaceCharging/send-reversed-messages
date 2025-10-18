import sys

def main():
    rev_paragraph(intake())


def intake():
    print("Enter your text, press Ctrl+D when done: ")
    return sys.stdin.read()
    # input() takes in one line. Here we need to take multiple lines as an input, so sys.stdin.read() is used.
    # sys.stdin.read() works like file open()


def rev(txt):
    return "".join(reversed(txt))
    # The reversed() function returns a reversed iterator, which is why a memory location was printed.
    # To get a string instead, convert it using ''.join().
    # A reversed iterator is an iterator that goes through the elements of a sequence in reverse order without creating a new list or string in memory.


def rev_paragraph(read_in):
    for line in read_in.splitlines():
        txt = rev(line)
        print(txt)


if __name__ == "__main__":
    main()


