#!/bin/bash
set -o errexit
printf "\nRunning code analysis...\n"
flake8 --show-source --exclude=generated/,.git/,__pycache__ .
printf "Code analysis passed.\n"
printf "\nRunning tests...\n"
nosetests -v --cover-branches --with-coverage --cover-erase --cover-html --cover-min-percentage=90 --cover-inclusive --cover-package=src
