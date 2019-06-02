#!/bin/sh

init_git() {
	git config --global user.email "db.update.bot@gmail.com"
	git config --global user.name "db-update-bot"
}

commit_files() {
	git checkout master
	git add *
	git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
	git config user.email
	git config user.name	
	git push
}

#init_git
commit_files
upload_files
