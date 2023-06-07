#Сourse work on the topic: Account transactions

#Job Description:
Code for the "Account Transactions" widget
The IT department of a large bank is making a new feature for the client's personal account. This is a widget that shows several recent successful banking transactions of the client. You have been entrusted to implement an algorithm that will prepare data for display in a new widget on the backend.

#Implements a function that displays a list of the last 5 operations performed by the client in the format:

<transfer date> <translation description>
<from where> -> <where>
<transfer amount> <currency>
    
 Virtual environment:
 # For Windows
python -m venv venv
# For Linux, macOS
python3 -m venv venv

 Аctivating the virtual environment:
.\venv\Scripts\activate

 Poetry Package Manager.
 # Windows
pip install poetry
# macOS
brew install poetry  
# Linux, macOS
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"

Testing with pytest
# Installation via Poetry
poetry add –G dev pytest

# Installation via pip
pip install pytest

#list of dependencies:
pytest 7.3.1 pytest: simple powerful testing with Python
├── colorama *
├── iniconfig *
├── packaging *
└── pluggy >=0.12,<2.0
pytest-cov 4.1.0 Pytest plugin for measuring coverage.
├── coverage >=5.2.1
└── pytest >=4.6
    ├── colorama *
    ├── iniconfig *
    ├── packaging *
    └── pluggy >=0.12,<2.0
Testing was done using pytest
