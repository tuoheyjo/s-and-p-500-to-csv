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
    header = table.find_all('th')

    if header[0].string != None or header[1].string != "Security":
        raise Exception("Can't parse wikipedia's table!")

    # Retreive the values in the table
    records = []
    rows = table.find_all('tr')
    for row in rows:
        fields = row.find_all('td')

        if fields:
            # remove \n characters that appear on travis-ci 
            for s in fields[0].stripped_strings:
                if (s != '\\n'):
                    symbol = s
            # remove \n characters that appear on travis-ci 
            for s in fields[1].stripped_strings:
                if (s != '\\n'):
                    name = s
            # remove \n characters that appear on travis-ci 
            for s in fields[3].stripped_strings:
                if (s != '\\n'):
                    sector = s
            # remove \n characters that appear on travis-ci 
            for s in fields[4].stripped_strings:
                if (s != '\\n'):
                    industry = s
            # remove \n characters that appear on travis-ci 
            for s in fields[5].stripped_strings:
                if (s != '\\n'):
                    hq = s
            first_added = ""
            # remove \n characters that appear on travis-ci 
            for s in fields[6].stripped_strings:
                first_added = s
                if (s != '\\n'):
                    first_added = s
            # remove \n characters that appear on travis-ci 
            for s in fields[7].stripped_strings:
                if (s != '\\n'):
                    CIK = s
            # remove \n characters that appear on travis-ci 
            for s in fields[8].stripped_strings:
                if (s != '\\n'):
                    founded = s
            records.append([symbol, name, sector, industry, hq, first_added, CIK, founded])

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

