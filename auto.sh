#!/bin/bash

git add -- . :!./daomain.py :!./daotwo.py
git commit -m "Update"
git push --all

