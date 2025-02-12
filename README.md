# Assignment 01

This assignment involves running shell commands, writing scripts, and processing data with Python.

#Folder Structure
root/ ├── _output/ │ ├── os.txt │ ├── cpu.txt │ ├── mem.txt │ ├── pip3.txt │ ├── jupyter.txt │ ├── count_python.sh │ └── count_github.py ├── README.md


---

#Tasks Overview
This project consists of three main tasks:
1️⃣, Collecting system information using shell commands
2️⃣, Witing a shell script to count occurrences of "Python" in StackOverflow data
3️⃣, Witing a Python script to count occurrences of "GitHub" in StackOverflow data

Each task is detailed below.

---

#Task 1: Collect System Information
The first task involves gathering information about the system and installed software.
The following commands were executed to generate system reports:

cat /etc/os-release > _output/os.txt
lscpu > _output/cpu.txt
lsmem > _output/mem.txt
pip3 --version > _output/pip3.txt
jupyter --version > _output/jupyter.txt

These files are stored in the _output/ folder.

---

#Task 2: Count "Python" Mentions
A shell script (count_python.sh) was created to count how many times the word "Python" appears in StackOverflow dataset CSV files.

How to Run:
./_output/count_python.sh

---

#Task 3: Count "GitHub" Mentions
A Python script (count_github.py) was created to count how many times the word "GitHub" appears in the dataset.

How to Run:
python3 _output/count_github.py

---

Author
Name: Jason Stopas
