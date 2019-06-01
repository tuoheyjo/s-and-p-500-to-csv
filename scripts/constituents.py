#!/usr/bin/python
from bs4 import BeautifulSoup
import csv
import sys
from os import mkdir
from os.path import exists, join
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


datadir = join('..', 'data')

if not exists(datadir):
    mkdir(datadir)

if not exists('tmp'):
    mkdir('tmp')

source = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
cache = join('tmp', 'List_of_S%26P_500_companies.html')

def retrieve():
    html = urlopen(source)
    page_content = html.read()
    with open(cache, 'w') as fid:
        fid.write(str(page_content))


def extract():
    source_page = open(cache).read()
    soup = BeautifulSoup(source_page, 'html.parser')
    table = soup.find("table", { "class" : "wikitable sortable" })

    # Fail now if we haven't found the right table
    header = table.findAll('th')
    #print(header[0].string, 'is', bool(header[0].string != None))
    #print(header[1].string, 'is', bool(header[1].string != "Security"))

    if header[0].string != None or header[1].string != "Security":
        raise Exception("Can't parse wikipedia's table!")

    # Retreive the values in the table
    records = []
    rows = table.findAll('tr')
    for row in rows:
        fields = row.findAll('td')
        if fields:
            symbol = fields[0].string
            # fix as now they have links to the companies on WP
            name = ' '.join(fields[1].stripped_strings)
            sector = fields[3].string
            records.append([symbol, name, sector])

    header = ['Symbol', 'Name', 'Sector']
    writer = csv.writer(open('../data/constituents.csv', 'w'), lineterminator='\n')
    writer.writerow(header)
    # Sorting ensure easy tracking of modifications
    records.sort(key=lambda s: s[1].lower())
    writer.writerows(records)    

def process():
    print("inside process function")
    retrieve()
    print("ran retrieve function")
    extract()
    print("ran extract function")

if __name__ == '__main__':
    process()

