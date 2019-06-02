#!/bin/sh

init_git() {
	git config --global user.email "travis@travis-ci.org"
	git config --global user.name "Travis CI"
}

commit_files() {
	git checkout master
	git add *
	git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
	git remote add origin https://${GITHUB_UPDATE_TOKEN}@github.com/flynneva/db_stock_functions.git
	git push
}

init_git
commit_files
upload_files
