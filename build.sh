#!/bin/sh

pipenv run pip freeze > requirements.txt
pipenv run pip install --target package/ -r requirements.txt
cd package
zip -r9 ../function.zip .
cd ..
zip -g function.zip *.py
