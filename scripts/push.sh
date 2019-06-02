#!/bin/sh

init_git() {
	git config --global user.email "db.update.bot@gmail.com"
	git config --global user.name "db-update-bot"
}

commit_files() {
	git checkout master
	git add . *.html
	git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
	git remote add master https://${GITHUB_UPDATE_TOKEN}@github.com/flynneva/db_stock_functions.git > /dev/null 2>&1
	git push --quiet --set-upstream
}

init_git
commit_files
upload_files
