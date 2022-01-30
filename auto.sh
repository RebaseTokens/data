#!/bin/bash

git add -- . :!./daomain.py :!./one.py :!./auto.py
git commit -m "Update"
git push --all

