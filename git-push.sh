#!/bin/bash

# Get the commit message from command line argument
commit_message="$1"

# Add all changes
git add .

# Commit changes with the provided message
git commit -m "$commit_message"

# Push changes to the remote repository
git push

