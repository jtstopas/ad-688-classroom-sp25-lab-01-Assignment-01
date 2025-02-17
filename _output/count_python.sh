#!/bin/bash

DATA_DIR=~/ad-688-classroom-sp25-lab-01-Assignment-01

count=$(grep -i "python" $DATA_DIR/*.csv | wc -l)

echo "Total lines containing 'python': $count"

