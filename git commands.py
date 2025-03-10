#to create new file or repository
git init
#to copy
git clone URL_link_of_code
#to check status of file when updated ,what updated, etc
git status
#to add code on git for continous updates
git add file_name_with_extension
#to commit or save or take screenshot of that code
git commit -m "message_why_you commit_or_take_screenshot"
#file inside which we store ignored file i.e. not useful file
.gitignore
#to commit all files 
git add .
#give summary of all activities we did previously
git log
#give summary in one line
git log --oneline
#give summary of how any lines are inserted,deleted and changed
git log --stat
#to get out of command
q
#to show all details of updates takes place in every file
git log -p
##to show all details of updates takes place in particular file
git show unique_id_of _commit_we_get_it_from_git log_--oneline
#to get info of line add and delete  before commit
git diff
#version of software (x.y.z) like ex. 3.9.1
#give version tag to a commit
git tag -a give_tag_name(ex. v1.0.0)   #then type text why to give tag in editor and save and quit
#give version tag to a commit
git tag -a give_tag_name(ex. v1.0.0)  unique_id_of _commit_we_get_it_from_git(i.e. sah from git log_--oneline)#then type text why to give tag in editor and save and quit
#to delete tag from a commit
gir tag -d give_tag_name(ex. v1.0.0)
#to create branches
git branch branch_name(ex. side_bar,login,etc)
#to check branches
git branch
#to create a branch of previous commit
git branch branch_name(ex. side_bar,login,etc) unique_id_of _commit_we_get_it_from_git log_--oneline(i.e. sah from git log_--oneline)
#to change to different branch
git checkout branch_name
#to see all commits including branches commit
git log --online --all
#to see all commits graphically
git log --online --all --graph
#to delete branch-branch couldn't be deleted if not merged 
git branch -d branch_name
#if want to delete branch anyway without merging
git branch -D branch_name
#to merge the current file to branced file
git merge file_name
#to give url where u want to push
git remote add origin copied_URL