#*Technical Documentation for Git & GitHub*
###Introduction
Git is a distributed version control system that allows developers to manage code changes effectively. GitHub is a cloud-based platform for hosting and collaborating on Git repositories.
###Setup & Configuration
Configure Git to identify yourself as a contributor:

Set Username:
git config --global user.name "[Your Name]"
Set Email:
git config --global user.email "[Your Email]"
Enable Color UI for Better Readability:
git config --global color.ui auto
###Repository Initialization & Cloning
Initialize a New Repository:
git init — Converts an existing folder into a Git repository.

Clone an Existing Repository:
git clone [repository URL] — Downloads a remote repository to your local machine.
###Staging & Commit
Stage and commit changes to track your work in Git.

Check Status:
git status — Shows modified files and their status.

Stage Files:
git add [file] — Adds files to the staging area.

Commit Changes:
git commit -m "[descriptive message]" — Saves staged changes with a commit message describing the work.
###Branching & Merging
Branches help manage multiple versions of a project.

List Branches:
git branch

Create a New Branch:
git branch [branch-name]

Switch to a Branch:
git checkout [branch-name]

Merge Branches:
git merge [branch-name]
###Branching & Merging
Branches help manage multiple versions of a project.

List Branches:
git branch

Create a New Branch:
git branch [branch-name]

Switch to a Branch:
git checkout [branch-name]

Merge Branches:
git merge [branch-name]
###Working with Remote Repositories
Collaborate by linking to a remote repository.

Add a Remote Repository:
git remote add [alias] [URL]

Push Changes to Remote:
git push [alias] [branch]

Pull Updates from Remote:
git pull
###Inspecting & Comparing
Examine changes, differences, and history.

View Commit History:
git log

Show Differences (Unstaged):
git diff

Show Differences (Staged):
git diff --staged
###Ignoring Files
Create a .gitignore file to exclude specific files from being tracked
###Advanced Git Commands
Stash Changes Temporarily:
git stash — Use when you want to save your changes without committing them.

Rebase Branch:
git rebase [branch] — This moves or combines a sequence of commits to a new base commit.



