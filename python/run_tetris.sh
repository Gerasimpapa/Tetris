#!/bin/bash
# Script για ενεργοποίηση virtual environment και εκτέλεση του Tetris στο WSL/Linux

# Χρώματα για output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Έλεγχος αν υπάρχει python3
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Σφάλμα: Το python3 δεν βρέθηκε!${NC}"
    echo "Τρέξτε: sudo apt update && sudo apt install python3 python3-venv python3-full"
    exit 1
fi

echo -e "${YELLOW}Tetris Game Launcher${NC}"
echo "===================="

# Έλεγχος αν το venv υπάρχει
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Δημιουργία virtual environment...${NC}"
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo -e "${RED}Σφάλμα: Δεν ήταν δυνατή η δημιουργία του virtual environment${NC}"
        echo "Δοκιμάστε: sudo apt install python3-full"
        exit 1
    fi
fi

# Ενεργοποίηση virtual environment
echo -e "${YELLOW}Ενεργοποίηση virtual environment...${NC}"
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo -e "${RED}Σφάλμα: Δεν βρέθηκε το venv/bin/activate${NC}"
    exit 1
fi

# Εγκατάσταση dependencies
echo -e "${YELLOW}Εγκατάσταση dependencies...${NC}"
pip install --upgrade pip
pip install -r requirements.txt

# Έλεγχος αν το pygame εγκαταστάθηκε
if python -c "import pygame" 2>/dev/null; then
    echo -e "${GREEN}Εκκίνηση Tetris...${NC}"
    python main.py
else
    echo -e "${RED}Σφάλμα: Το pygame δεν εγκαταστάθηκε με επιτυχία${NC}"
    exit 1
fi

# Απενεργοποίηση virtual environment
deactivate
