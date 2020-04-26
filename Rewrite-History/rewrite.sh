#!/bin/bash

yesterday="$(date +'%F %T' --date=yesterday)"

# Set git env vars
export GIT_COMMITTER_DATE=$yesterday
export GIT_AUTHOR_DATE=$yesterday

printf "[WARNING]: Git dates set to $yesterday\n"
printf "           RESTART SHELL TO RESET DATES\n"
