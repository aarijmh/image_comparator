@echo off
echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
python -m pip install --upgrade pip
pip install -e .

echo Setup complete! To start the application:
echo 1. Activate the virtual environment: venv\Scripts\activate
echo 2. Run the application: python app.py
echo 3. Open http://localhost:5000 in your browser

pause
