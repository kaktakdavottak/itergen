import wikipedia
import json


class CountriesIter:
    def __init__(self, file):
        with open(file, encoding='utf-8') as f:
            self.json_data = json.load(f)
        self.start = 0
        self.end = len(self.json_data)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        try:
            country_name = self.json_data[self.start - 1]["name"]["common"]
            try:
                country_page = wikipedia.page(country_name)
            except wikipedia.exceptions.DisambiguationError:
                country_page = wikipedia.page(country_name + '(country)')
            country_url = country_page.url
            res = country_name + ' - ' + country_url

            with open('result_countries.txt', 'a', encoding='utf-8') as f:
                f.write(res + '\n')

            if self.start > self.end:
                raise StopIteration

            return res

        except IndexError:
            raise StopIteration


if __name__ == "__main__":
    for countries in CountriesIter('countries.json'):
        print(countries)
