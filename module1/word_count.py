#print(__name__)
"""Read file from web and do analysis of data
"""
# borrowing code style from: 
# https://realpython.com/python-web-scraping-practical-introduction/#use-an-html-parser-for-web-scraping-in-python

from urllib.request import urlopen


def count_words_from_web_file(url_address):
    words = 0
    # Read file from web
    with urlopen(url_address) as data: #shortcut: we could do data =... but that would also use open() and close()
        for line in data:
            # print(line, type(line))
            print(line.decode('utf-8'), type(line))
            line_words = line.split() # space is default delimiter in split()
            for word in line_words:
                # Count number of words
                words = words + 1

    return words

def main():
    """Driven Function
    """
    #website = urlopen.Request('https://icarus.cs.weber.edu/~hvalle/sample_data/poem.txt')
    #html = website.read().decode("utf-8")
    file_address = 'https://icarus.cs.weber.edu/~hvalle/sample_data/poem.txt'
    total_words = count_words_from_web_file(file_address)
    print(f'There are a total of {total_words} in the file')

if __name__ == '__main__':
    main() # if the value is = to main then call this entry point