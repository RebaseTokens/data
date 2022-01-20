#!/bin/bash

git add -- . :!./daomain.py
git commit -m "Update"
git push --all

