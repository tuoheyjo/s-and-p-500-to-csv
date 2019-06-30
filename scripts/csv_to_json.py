#!/usr/bin/python
import csv
import json
import sys
from os import mkdir, remove
from os.path import join, exists, dirname

dirpath = dirname(sys.path[0])
datadir = join(dirpath, 'data')
fpathjson = join(datadir, 'sp500.json')
fpathcsv = join(datadir, 'sp500.csv')

if (exists(datadir)):
    try:
        remove(fpath)
    except:
        print("/data directory empty...continue on...")
else:
    mkdir(datadir)

if not exists('tmp'):
    mkdir('tmp')

def csv_to_json():
    # Open the CSV
    with open(fpathcsv, 'rU') as f:
        # get the header row for the dictionary field names
        reader = csv.reader(f)
        headers = next(reader)
        # assign dictionary field names
        dictReader = csv.DictReader( f, headers)
        # parse the csv data to json
        out = json.dumps( [ row for row in dictReader ] )

    # save the json
    f = open(fpathjson, 'w')
    f.write(out)
    print("JSON saved!")

if __name__ == '__main__':
    csv_to_json()
