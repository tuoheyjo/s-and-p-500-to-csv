all: ../data/constituents.csv

../data:
	mkdir ../data    
    
../data/constituents.csv: ../data constituents.py
	python constituents.py
	python csv_to_json.py
.PHONY: all
