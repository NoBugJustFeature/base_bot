@echo off

echo Creating virtual environment...
python -m venv env
env\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo Creating .env file for environment variables...
type .env.example > .env

echo Done!
