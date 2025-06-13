#!/bin/bash

# Check if a commit message was passed as an argument
if [ -z "$1" ]; then
  read -p "Enter commit message: " commitmsg
else
  commitmsg="$1"
fi

# Git operations
git add .
git commit -m "$commitmsg"
git push
