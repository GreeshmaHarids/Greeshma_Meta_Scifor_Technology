<h1>Technical Documentation for Git & GitHub</h1>

<h3>Introduction</h3>

Git is a distributed version control system that allows developers to manage code changes effectively. GitHub is a cloud-based platform for hosting and collaborating on Git repositories.

<h3>Setup & Configuration</h3>
Configure Git to identify yourself as a contributor:

Set Username:
*git config --global user.name "[Your Name]"*

Set Email:
*git config --global user.email "[Your Email]"*

Enable Color UI for Better Readability:
*git config --global color.ui auto*

<h3>Repository Initialization & Cloning</h3>
Initialize a New Repository:
*git init* — Converts an existing folder into a Git repository.

Clone an Existing Repository:
*git clone [repository URL]* — Downloads a remote repository to your local machine.

<h3>Staging & Commit</h3>
Stage and commit changes to track your work in Git.

Check Status:
*git status* — Shows modified files and their status.

Stage Files:
*git add [file]* — Adds files to the staging area.

Commit Changes:
*git commit -m "[descriptive message]"* — Saves staged changes with a commit message describing the work.

<h3>Branching & Merging</h3>
Branches help manage multiple versions of a project.

List Branches:
*git branch*

Create a New Branch:
*git branch [branch-name]*

Switch to a Branch:
*git checkout [branch-name]*

Merge Branches:
*git merge [branch-name]*

<h3>Working with Remote Repositories</h3>
Collaborate by linking to a remote repository.

Add a Remote Repository:
*git remote add [alias] [URL]*

Push Changes to Remote:
*git push [alias] [branch]*

Pull Updates from Remote:
*git pull*

<h3>Inspecting & Comparing</h3>
Examine changes, differences, and history.

View Commit History:
*git log*

Show Differences (Unstaged):
*git diff*

Show Differences (Staged):
*git diff --staged*

<h3>Ignoring Files</h3>
Create a .gitignore file to exclude specific files from being tracked

<h3>Advanced Git Commands</h3>
Stash Changes Temporarily:

*git stash* — Use when you want to save your changes without committing them.

Rebase Branch:
*git rebase [branch]* — This moves or combines a sequence of commits to a new base commit.

<h2>GitHub</h2>

*Commits*: Snapshots of code changes. Write clear messages to explain each change.

*Pull Requests*: Propose changes for review before merging into the main branch.

*Forking*: Copy another repo to your GitHub to make changes or contribute back with a pull request.

*Issues*: Track bugs, features, and tasks; link commits by mentioning issue numbers.

*GitHub Actions*: Automate workflows like testing and deployment when code changes are pushed.



