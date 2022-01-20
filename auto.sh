#!/bin/bash

git add -- . :!./daomain.py :!./daotwo.py :!./geckodriver.log
git commit -m "Update"
git push --all

