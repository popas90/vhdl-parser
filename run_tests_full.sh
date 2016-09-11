#!/bin/bash
set -o errexit
printf "Running code analysis...\n"
flake8 --show-source --exclude=generated/,.git/,__pycache__ .
printf "Code analysis passed.\n"
printf "\nRunning tests...\n"
nosetests -v --with-coverage --cover-erase --cover-html --cover-min-percentage=100 --cover-inclusive --cover-package=src
