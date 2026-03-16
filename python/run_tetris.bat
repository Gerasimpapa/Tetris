@echo off
REM Script για ενεργοποίηση virtual environment και εκτέλεση του Tetris

REM Έλεγχος αν το venv υπάρχει
if not exist "venv" (
    echo Δημιουργία virtual environment...
    python -m venv venv
)

REM Ενεργοποίηση virtual environment
echo Ενεργοποίηση virtual environment...
call venv\Scripts\activate.bat

REM Εγκατάσταση dependencies (αν δεν υπάρχουν)
echo Εγκατάσταση dependencies...
pip install -r requirements.txt

REM Εκτέλεση game
echo Εκκίνηση Tetris...
python main.py

REM Απενεργοποίηση virtual environment
deactivate
