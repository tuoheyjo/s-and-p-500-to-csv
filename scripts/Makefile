all: ../data/sp500.csv

../data:
	mkdir ../data    
    
../data/sp500.csv: ../data get_sp500.py
	python get_sp500.py
	python csv_to_json.py
	python upload_firebase.py
.PHONY: all
