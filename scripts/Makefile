all: pushed.txt

../data:
	mkdir ../data    
    
../data/constituents.csv: ../data constituents.py
	python constituents.py


pushed.txt: ../data/constituents.csv
	git checkout master
	git add * 
	git commit -m "automatic update" || exit 0
	git push
	echo "Update has been pushed if there was a change" > pushed.txt

.PHONY: all
