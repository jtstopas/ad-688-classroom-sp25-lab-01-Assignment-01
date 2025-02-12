#!/bin/bash
echo "Counting lines containing 'python' in StackOverflow data..."
count=$(grep -i "python" *.csv | wc -l)
echo "Total lines with 'python': $count"
