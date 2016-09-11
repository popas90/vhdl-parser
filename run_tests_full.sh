#!/bin/bash
flake8 --show-source --exclude=generated/,.git/,__pycache__ .
nosetests -v --with-coverage --cover-erase --cover-html --cover-min-percentage=100 --cover-inclusive --cover-package=src
