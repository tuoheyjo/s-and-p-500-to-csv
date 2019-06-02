#!/usr/bin/python
from bs4 import BeautifulSoup
import csv
import sys
import re
from os import mkdir, remove
from os.path import exists, join
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


datadir = join('..', 'data')

if (exists(datadir)):
    try:
        remove(join(datadir, 'constituents.csv'))
    except:
        print("/data directory empty...continue on...")
else:
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
    source_page = open(cache, 'r').read()
    soup = BeautifulSoup(source_page, 'html.parser')
    table = soup.find("table", { "class" : "wikitable sortable" })

    # Fail now if we haven't found the right table
    header = table.findAll('th')

    if header[0].string != None or header[1].string != "Security":
        raise Exception("Can't parse wikipedia's table!")

    # Retreive the values in the table
    records = []
    rows = table.findAll('tr')
    for row in rows:
        fields = row.findAll('td')

        if fields:
            
            symbol = fields[0].text.strip('\n')
            print(symbol)
            print(symbol[:2])
            # fix as now they have links to the companies on WP
            name = str(fields[1].get_text())
            sector = fields[3].text.strip('\n')
            industry = fields[4].text.strip('\n')
            hq = fields[5].text.strip('\n')
            first_added = fields[6].text.strip('\n')
            CIK = fields[7].text.strip('\n')
            founded = fields[8].text.strip('\n')

            records.append([symbol, name, sector, industry, hq.encode('UTF-8'), first_added, CIK, founded])

    header = ['Symbol', 'Name', 'Sector', 'SubIndustry', 'Headquarters_Location', 'Date_First_Added', 'CIK', 'Founded']
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

