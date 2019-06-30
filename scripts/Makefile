all: ../data/sp500.csv

../data:
	mkdir ../data    
    
../data/sp500.csv: ../data sp500.py
	python sp500.py
	python csv_to_json.py
	python upload_firebase.py
.PHONY: all
