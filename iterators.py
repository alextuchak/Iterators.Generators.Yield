import json
import re
from pprint import pprint
class CountriesLinks:

    def get_names(self):
        with open('countries.json') as f:
            temp = json.load(f)
            return temp

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.get_names()):
            raise StopIteration
        country_names = self.get_names()[self.cursor]['name']['official']
        link = 'https://en.wikipedia.org/wiki/' + re.sub("'", '', re.sub(' ', '_', country_names))
        with open('countries_and_links', 'a', encoding='utf-8') as f:
            f.write(f'{country_names} - {link}\n')
        return f'{country_names} - {link}\n'


def main():
    for country_names in CountriesLinks():
        print(country_names)


if __name__ == '__main__':
    main()


