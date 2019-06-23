#!/usr/bin/python
import csv
import json
import sys
from os import mkdir, remove
from os.path import join, exists, dirname

dirpath = dirname(sys.path[0])
datadir = join(dirpath, 'data')
fpathjson = join(datadir, 'constituents.json')
fpathcsv = join(datadir, 'constituents.csv')

if (exists(datadir)):
    try:
        remove(fpath)
    except:
        print("/data directory empty...continue on...")
else:
    mkdir(datadir)

if not exists('tmp'):
    mkdir('tmp')

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
print "JSON saved!"

# Get the header row as field names

# parse data

# save file

