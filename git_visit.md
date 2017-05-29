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

- git diff: show changes added but not staged yet

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
