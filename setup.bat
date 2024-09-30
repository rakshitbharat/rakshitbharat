@echo off

REM Create a virtual environment
python -m venv venv

REM Activate the virtual environment
call venv\Scripts\activate

REM Install the required packages
pip install -r requirements.txt

echo Virtual environment setup complete. Activate it with 'venv\Scripts\activate'