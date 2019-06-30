#!/bin/sh

init_git() {
	git config --global user.email "db.update.bot@gmail.com"
	git config --global user.name "db-update-bot"
}

commit_files() {
	git checkout master
	git add ../data/sp500.csv
	git add ../data/sp500.json
	git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
	# Remove existing "origin"
	git remote rm origin
	# Add new "origin" with access token in the git URL for authentication
	git remote add origin https://db-update-bot:${GITHUB_TOKEN}@github.com/flynneva/s-and-p-500-to-csv.git > /dev/null 2>&1
	git push origin master --quiet
}

init_git
commit_files
upload_files
