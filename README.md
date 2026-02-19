📘 Code Documentation Navigator
A lightweight web-based tool that scans Python projects and allows you to:
🔍 Search functions and classes


📂 View source files


🎨 See syntax-highlighted code


⚡ Navigate project structure easily



📌 Table of Contents
Project Overview


Features


System Architecture


Installation Guide


Usage Guide


Project Structure


How It Works


Security Measures


Future Improvements


License



1️⃣ Project Overview
Code Documentation Navigator is a Flask-based web application that automatically scans a directory for Python files and extracts:
Classes


Functions


It builds an internal index and allows users to search and browse code through a simple web interface.

2️⃣ Features
✅ Code Indexing
Automatically scans .py files


Extracts function and class names


Uses Python AST for accurate parsing


✅ Smart Search
Case-insensitive search


Partial match support


Displays file path and symbol type


✅ File Viewer
View complete source file


Syntax highlighting enabled


Clean UI


✅ Secure File Access
Prevents directory traversal attacks


Only allows project directory access



3️⃣ System Architecture
User Browser
     ↓
Flask Web Server (app.py)
     ↓
CodeIndexer (indexer.py)
     ↓
Python AST Parser
     ↓
Indexed Symbol Database (in memory)

Components
Component
Description
app.py
Main Flask server
indexer.py
Code parsing & search logic
templates/
HTML UI
static/
CSS styling


4️⃣ Installation Guide
Step 1: Clone Repository
git clone https://github.com/lakshyabhardwaj0705-gif/scaledown-2.git
cd scaledown-2

Step 2: Create Virtual Environment (Recommended)
python -m venv venv

Activate:
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Run Application
python app.py

Open in browser:
http://127.0.0.1:5000


5️⃣ Usage Guide
🔍 Searching for Code
Enter function or class name in search bar


Click Search


View results list


📂 Viewing File
Click "View File"


Syntax highlighted code appears


Use Back button to return



6️⃣ Project Structure
scaledown-2/
│
├── app.py                # Main Flask application
├── indexer.py            # Code indexing engine
├── requirements.txt      # Python dependencies
├── README.md             # Documentation
├── .gitignore
│
├── templates/
│   ├── index.html        # Search page
│   └── file.html         # File viewer
│
└── static/
    └── style.css         # Styling



