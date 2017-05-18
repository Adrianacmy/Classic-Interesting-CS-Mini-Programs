##
- don't change anything in .git except the hook
- git clone url_to_clone_project new_folder_name: clone and rename the project
- git log --stat : with number of chnagd lines
- git log --oneline 
- git log --p : show the acctual changes, it  is the most detailed
- git show SHA
- git log -p SHA

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
