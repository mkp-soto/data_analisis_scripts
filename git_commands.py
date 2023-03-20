# print working directory
$ pwd
# list files in folder
$ ls
# initialize git repository locally
$ git init
# add all files inside folder to git
$ git add .
# commit
$ git commit -m "first commit"
# connect to remote repository (online repo must be set up first)
$ git remote add origin https://github.com/mkp-soto/studying_data_analysis.git
# push commit to remote repo (origin) in the branch master
$ git push -u origin master
# check the branches of the project
$ git branch
# create new branch
$ git branch -c dev
# change to other branch
$ git checkout dev
# merge dev branch into master
$ git checkout master
$ git merge dev
# update remote master branch
$ git push -u origin master
