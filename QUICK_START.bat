@echo off
echo ========================================
echo AI Legal Chatbot - Quick Start
echo ========================================
echo.

echo Step 1: Setting up Python virtual environment...
if not exist venv (
    python -m venv venv
    echo Virtual environment created!
) else (
    echo Virtual environment already exists.
)

echo.
echo Step 2: Activating virtual environment...
call venv\Scripts\activate

echo.
echo Step 3: Installing Python dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Step 4: Running web scraper...
python backend\scraper\scrape_legal_data.py

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the application:
echo   1. Backend: python backend\main.py
echo   2. Frontend: cd frontend ^&^& npm install ^&^& npm start
echo.
echo Press any key to start the backend server...
pause

python backend\main.py

