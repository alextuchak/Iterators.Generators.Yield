import hashlib


def main(countries_and_links):
    with open(countries_and_links, 'r') as f:
        strings = f.readlines()
        for string in strings:
            yield hashlib.md5(string.encode()).hexdigest()


if __name__ == '__main__':
    for string in main('countries_and_links'):
        print(string)