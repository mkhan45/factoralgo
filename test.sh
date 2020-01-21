#!/bin/sh
for f in *.py
do
   python "$f" "$1"
done
