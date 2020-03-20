from bs4 import BeautifulSoup
import itertools 

class Kursy:
    def __init__(self, path):
        self.soup = self.read_file(path)
        self.currency_dict = self.currency_dict(self.soup)
        self.currency_list = self.currency_list(self.soup)
       
    def read_file(self, path):
        with open(path) as file:
            soup = BeautifulSoup(file, 'html.parser') 
        return soup

    def currency_dict(self, soup):
        currency_codes = [code.string for code in soup.find_all('kod_waluty')]
        currency_values = [float(str(value.string).replace(',', '.')) for value in soup.find_all('kurs_sredni')]
        currency_dict = dict(itertools.zip_longest(currency_codes, currency_values))
        return currency_dict
    
    def currency_list(self, soup):
        currency_names = [name.string for name in soup.find_all('nazwa_waluty')]
        currency_codes = [code.string for code in soup.find_all('kod_waluty')]
        currency_list = dict(itertools.zip_longest(currency_names, currency_codes))
        return currency_list
        
    def convert_from_pln(self, from_value, to_name):
        if not to_name in self.currency_dict:
            print('Brak informacji o kursie tej waluty.')
        currency_codes = [code.string for code in self.soup.find_all('kod_waluty')]
        converter = [int(converter.string) for converter in self.soup.find_all('przelicznik')]
        currency_converter = dict(itertools.zip_longest(currency_codes, converter))
        return (from_value / self.currency_dict[to_name]) * currency_converter[to_name]

    def convert_to_pln(self, from_value, from_name):
        if not from_name in self.currency_dict:
            print('Brak informacji o kursie tej waluty')
        currency_codes = [code.string for code in self.soup.find_all('kod_waluty')]
        converter = [int(converter.string) for converter in self.soup.find_all('przelicznik')]
        currency_converter = dict(itertools.zip_longest(currency_codes, converter))
        return (from_value * self.currency_dict[from_name]) / currency_converter[from_name]

    def from_one_to_another(self, from_value, from_name, to_name):
        to_pln = self.convert_to_pln(from_value, from_name)
        converted = self.convert_from_pln(to_pln, to_name)
        return converted