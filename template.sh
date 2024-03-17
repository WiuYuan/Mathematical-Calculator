#!/bin/bash
set -e
set -u
set -o pipefail

/Users/yuanwen/anaconda3/envs/env_early/bin/python /Users/yuanwen/Desktop/test/project/calculator_write.py

xelatex calculator_show.tex -synctex=1 -interaction=nonstopmode -file-line-error

rm *.aux *.log *.synctex.gz