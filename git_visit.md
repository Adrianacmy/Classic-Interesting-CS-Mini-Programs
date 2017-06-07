##
- don't change anything in .git except the hook
- git clone url_to_clone_project new_folder_name: clone and rename the project
- git log --stat : with number of chnagd lines
- git log --oneline 
- git log --p : show the acctual changes, it  is the most detailed
- git show SHA
- git log -p SHA
- git reflog ?

git config --global core.editor "atom --wait"

### how to write a good commit msg:
- short
- explain what does the commit do
- don't explain how and why
- don't use 'and', keep one change one commit
- eg : This commit will....
- see [udacity commit msg style guide](https://udacity.github.io/git-styleguide/)

- git diff: show changes added but not staged yet?

- glob for .gitignore
    --blank lines can be used for spacing
    -- # - marks line as a comment
    --* - matches 0 or more characters
    --? - matches 1 character
    --[abc] - matches a, b, or c
    --** - matches nested directories - a/**/z matches
        -a/z
        -a/b/z
        -a/b/c/z


- git tag -a v1.0 (a: annoted): add a tag for latest commit
- git tag -a v1.0 SHA: add a tag for certain commits happened
- git tag -d v1.0: delete a tag
- git log --decorate : see log with tags

- git branch algo SHA : create a branch at commit SHA named algo
- git branch -d algo: have to switch to other branch and then delete algo
- git checkout -b algo master: create and switch to algo whick got the same
        location as master
- git log --oneline -- decorate -- graph --all

- git reset --hard HEAD^ : undo last merge on the wrong branch

- merge conflict:
    <<<<<<< HEAD everything below this line (until the next indicator) shows 
        you what's on the current branch
    ||||||| merged common ancestors everything below this line (until the next
         indicator) shows you what the original lines were
    ======= is the end of the original lines, everything that follows (until 
        the next indicator) is what's on the branch that's being merged in
    >>>>>>> heading-update is the ending indicator of what's on the branch
         that's being merged in (in this case, the heading-update branch)

- git commit --amend: fix the most recent commit
- git commit --amend --no-edit: make amendment without changing the commit msg
- git revert SHA : undo changes of SHA commit and create a new commit to record
    the change


- git rebase
- git rebase -i
- git reset --soft|--hard|--mixed HEAD

 ~ – indicates the first parent commit
 ^ – indicates the parent commit

    The main difference between the ^ and the ~ is when a commit is created from a
    merge. A merge commit has two parents. With a merge commit, the ^ reference 
    is used to indicate the first parent of the commit while ^2 indicates the 
    second parent. The first parent is the branch you were on when you ran git 
    merge while the second parent is the branch that was merged in.

- git remote add remote_name remote_url
- git remote remove(rm) remote-name: remove remote while stop contributing eg.
- git remote -v : show all remote with detailed url and shortname
- git remote show [remote-name]: show all remote details and local push target branches

Change your remote's URL from SSH to HTTPS with the git remote set-url command.
- git remote set-url origin https://github.com/USERNAME/REPOSITORY.git: switch



- git pull origin master
    retrieves commits
    move the tracking branch to above commits
    merge local branch with the tracking branch

- git fetch origin master: retrieves commits and move the tracking branch

- git shortlog -s -n: show commits numbers(-s) of all authors ordered by number(-n)
- git log --author="Adriana": show certain author's commits
- git log --grep bug
- git log --grep="Adriana fix": filter commits with keywords of 'Adriana fix'
        cautious about the space and quotes when there are more than one keywords

- git stash
    git stash list
    git stash pop
    git stash apply {stash name}

    When to Stash

    Stashing helps you get a clean working copy. While this can be helpful in
     many situations, it's strongly recommended...
    ...before checking out a different branch.
    ...before pulling remote changes.
    ...before merging or rebasing a branch.

## How to contribute

Before you start doing any work, make sure to look for the project's CONTRIBUTING.md 
file.

Next, it's a good idea to look at the GitHub issues for the project

    - look at the existing issues to see if one is similar to the change you want
    to contribute if necessary create a new issue
    
    - communicate the changes you'd like to make to the project maintainer in the
    issue
    
When you start developing, commit all of your work on a topic branch:
    - do not work on the master branch
    - make sure to give the topic branch clear, descriptive name
    
As a general best practice for writing commits:
    - make frequent, smaller commits
    - use clear and descriptive commit messages
    - update the README file, if necessary

A pull request is a request for the source repository to pull in your commits
and merge them with their project. To create a pull request, a couple of things
need to happen:
    - you must fork the source repository
    - clone your fork down to your machine
    - make some commits (ideally on a topic branch!)
    - push the commits back to your fork
    - create a new pull request and choose the branch that has your new commits


When working with a project that you've forked. The original project's maintainer
will continue adding changes to their project. You'll want to keep your fork of 
their project in sync with theirs so that you can include any changes they make.

To get commits from a source repository into your forked repository on GitHub you 
need to:

    - get the cloneable URL of the source repository
    - create a new remote with the git remote add command

        - use the shortname upstream to point to the source repository
        - provide the URL of the source repository

    - fetch the new upstream remote
    - merge the upstream's branch into a local branch
    - push the newly updated local branch to your origin repo


