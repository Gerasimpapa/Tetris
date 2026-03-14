# Tetris Game

Ένα κλασικό παιχνίδι Tetris γραμμένο σε Python με Pygame.

## 📋 Περιγραφή Project

Αυτό το project είναι μια υλοποίηση του παγκοσμίως γνωστού παιχνιδιού Tetris. Το παιχνίδι έχει πλήρη λειτουργικότητα με collision detection, rotation, line clearing, scoring system και game over detection.

## 📁 Δομή Αρχείων

```
Tetris/
├── main.py              # Entry point του παιχνιδιού (ξεκίνημα)
├── game.py              # Κύριο game logic (κανόνες, updates, collision)
├── pieces.py            # Ορισμοί Tetromino pieces (τα κομμάτια)
├── renderer.py          # Pygame rendering (σχεδίαση γραφικών)
├── constants.py         # Σταθερές & χρώματα (configurations)
├── requirements.txt     # Dependencies (εξαρτήσεις)
├── run_tetris.bat       # Windows convenience script
├── run_tetris.sh        # WSL/Linux convenience script
├── .gitignore           # Git ignore file
└── README.md            # Αυτό το αρχείο
```

## 📝 Περιγραφή Αρχείων

### `main.py`
Είναι το **κύριο αρχείο εκτέλεσης**. Περιέχει την κύρια εφαρμογή `TetrisApplication` και τον game loop που:
- Διαχειρίζεται τα events (πατήματα πλήκτρων)
- Ενημερώνει το game state
- Αποδίδει τα γραφικά

### `game.py`
Περιέχει την κλάση `TetrisGame` με **όλη τη λογική του παιχνιδιού**:
- `update()` - Ενημέρωση game state σε κάθε frame
- `move_piece_down()` - Πτώση κομματιού
- `move_piece_left/right()` - Πλευρική κίνηση
- `rotate_piece()` - Περιστροφή κομματιού
- `hard_drop()` - Άμεση πτώση στο κάτω μέρος
- `is_valid_position()` - Έλεγχος αν η θέση είναι έγκυρη
- `lock_piece()` - Κλείδωμα κομματιού στο board
- `check_lines()` - Έλεγχος και διαγραφή γεμάτων σειρών
- `spawn_new_piece()` - Δημιουργία νέου κομματιού

### `pieces.py`
Ορίζει **τα 7 Tetromino κομμάτια** (I, O, T, S, Z, J, L):
- `PIECE_SHAPES` - Αρχικά σχήματα
- `ROTATIONS` - Περιστροφές για κάθε κομμάτι
- Κλάση `Piece` με μεθόδους για κίνηση, περιστροφή και undo

### `renderer.py`
Ευθύνεται για **την αποτύπωση γραφικών** χρησιμοποιώντας Pygame:
- `draw_game()` - Αποτύπωση όλου του παιχνιδιού
- `draw_grid()` - Σχεδίαση πλέγματος
- `draw_board()` - Σχεδίαση κλειδωμένων κομματιών
- `draw_piece()` - Σχεδίαση πτώσης κομματιού
- `draw_sidebar()` - Σχεδίαση πλευρικής μπάρας με score & next piece
- `draw_game_over()` - Οθόνη game over

### `constants.py`
**Κεντρικές ρυθμίσεις του παιχνιδιού**:
- Διαστάσεις board (10x20)
- Μέγεθος κελιού (CELL_SIZE = 30 pixels)
- Χρώματα για κάθε κομμάτι
- Game states (PLAYING, PAUSED, GAME_OVER)
- Fall speed

## 🚀 Εγκατάσταση & Εκτέλεση

### ⚡ Γρήγορη Εκκίνηση (Προτεινόμενο)

#### Windows - Με Ένα Click
Απλά **διπλοκλικάρετε** το αρχείο `run_tetris.bat`:
- ✅ Δημιουργεί το virtual environment (αν δεν υπάρχει)
- ✅ Ενεργοποιεί το virtual environment
- ✅ Εγκαθιστά τα dependencies
- ✅ Εκτελεί το παιχνίδι

**Ή** από PowerShell:
```powershell
.\run_tetris.bat
```

#### WSL/Linux - Με Ένα Εντολή
```bash
bash run_tetris.sh
```

---

### Σύστημα Windows (PowerShell)

#### 1. Εγκατάσταση Dependencies (Απλή Μέθοδος - Χωρίς Virtual Environment)

Αν δεν θέλετε να χρησιμοποιήσετε virtual environment:

```powershell
cd "g:\My Drive\Projects\Programs\Tetris"
pip install -r requirements.txt
python main.py
```

#### 2. Με Virtual Environment (Προτεινόμενο)

Δημιουργία και χρήση ενός isolated Python environment:

**Δημιουργία Virtual Environment:**
```powershell
cd "g:\My Drive\Projects\Programs\Tetris"
python -m venv venv
```

**Ενεργοποίηση Virtual Environment:**
```powershell
# Στο PowerShell:
.\venv\Scripts\Activate.ps1
```

Αν έχετε σφάλμα για execution policy, τρέξτε:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Μετά την ενεργοποίηση, θα δείτε `(venv)` στην αρχή της γραμμής:
```powershell
(venv) PS G:\My Drive\Projects\Programs\Tetris>
```

**Εγκατάσταση Dependencies:**
```powershell
pip install -r requirements.txt
```

**Εκτέλεση Παιχνιδιού:**
```powershell
python main.py
```

**Απενεργοποίηση Virtual Environment:**
```powershell
deactivate
```

### Σύστημα Linux/WSL (Windows Subsystem for Linux)

#### ⚠️ Προαπαιτούμενα για WSL

Πρώτα, ενημερώστε το σύστημά σας και εγκαταστήστε τα απαραίτητα πακέτα:

```bash
# Ανοίξτε WSL και τρέξτε:
sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-venv python3-full python3-pip -y
```

#### 1. Ανοίξτε WSL terminal
```bash
wsl
```

#### 2. Πλοήγηση στο directory
```bash
cd "/mnt/g/My Drive/Projects/Programs/Tetris"
# ή
cd "/mnt/g/MyDrive/Projects/Programs/Tetris"
```

#### 3. Με Το Convenience Script (Προτεινόμενο)

Απλή εντολή:
```bash
bash run_tetris.sh
```

Το script κάνει **αυτόματα όλα**:
- ✅ Δημιουργεί το virtual environment
- ✅ Ενεργοποιεί το venv
- ✅ Εγκαθιστά dependencies
- ✅ Εκτελεί το παιχνίδι

#### 4. Χειροκίνητη Setup (Αν θέλετε περισσότερο έλεγχο)

**Δημιουργία Virtual Environment:**
```bash
python3 -m venv venv
```

**Ενεργοποίηση:**
```bash
source venv/bin/activate
```

Θα δείτε `(venv)` στην αρχή της γραμμής:
```bash
(venv) user@computer:/path/to/Tetris$
```

**Εγκατάσταση dependencies:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Εκτέλεση:**
```bash
python main.py
```

**Απενεργοποίηση:**
```bash
deactivate
```

**⚠️ Σημείωση για WSL:** Το παιχνίδι χρειάζεται X11 display server για να εμφανίσει γραφικά. Μπορείτε:
- Να εγκαταστήσετε VcXsrv ή Xming στα Windows
- Ή να χρησιμοποιήσετε το native Windows Python (πιο απλό)

**💡 Συμβουλή:** Χρησιμοποιήστε το native Windows PowerShell για αποφυγή προβλημάτων με τα γραφικά.

## 🎮 Οδηγίες Χρήσης

### Τρέχοντας το Παιχνίδι

1. Ανοίξτε PowerShell (ή WSL)
2. Πλοηγηθείτε στο folder του Tetris
3. Τρέξτε: `python main.py`
4. Ένα παράθυρο Pygame θα ανοίξει με το παιχνίδι

### Default Key Bindings (Προεπιλεγμένες Εντολές)

| Πλήκτρο | Ενέργεια |
|---------|----------|
| **←** | Κίνηση κόμματος αριστερά |
| **→** | Κίνηση κόμματος δεξιά |
| **↓** | Γρήγορη πτώση |
| **SPACE** | Περιστροφή κομματιού |
| **↑** | Hard drop (πάνω στο κάτω μέρος) |
| **P** | Pause/Resume |
| **R** | Restart game |
| **Q** / **ESC** | Quit |

## 🔧 Αλλαγή Key Bindings

Τα key bindings βρίσκονται στο αρχείο **`main.py`** στη μέθοδο `handle_events()`.

### Εντοπισμός Κωδικού

Ανοίξτε το `main.py` και ψάξτε για τη μέθοδο:

```python
def handle_events(self):
    """Handle user input and events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self.running = False
        
        elif event.type == pygame.KEYDOWN:
            # ... Key bindings εδώ
```

### Παραδείγματα Αλλαγής

#### Παράδειγμα 1: Αλλαγή του Pause key από P σε O

Βρείτε:
```python
if event.key == pygame.K_p:
    # Pause/unpause
```

Αλλάξτε σε:
```python
if event.key == pygame.K_o:
    # Pause/unpause
```

#### Παράδειγμα 2: Αλλαγή του Hard drop από ↑ σε D

Βρείτε:
```python
elif event.key == pygame.K_UP:
    self.game.hard_drop()
```

Αλλάξτε σε:
```python
elif event.key == pygame.K_d:
    self.game.hard_drop()
```

### Διαθέσιμα Pygame Keys

```python
# Βασικά πλήκτρα
pygame.K_UP           # Πάνω βέλος
pygame.K_DOWN         # Κάτω βέλος
pygame.K_LEFT         # Αριστερό βέλος
pygame.K_RIGHT        # Δεξί βέλος
pygame.K_SPACE        # Space bar
pygame.K_RETURN       # Enter
pygame.K_ESCAPE       # Escape

# Γράμματα A-Z
pygame.K_a through pygame.K_z

# Αριθμοί 0-9
pygame.K_0 through pygame.K_9

# Επιπλέον πλήκτρα
pygame.K_LSHIFT       # Αριστερό Shift
pygame.K_RSHIFT       # Δεξί Shift
pygame.K_LCTRL        # Αριστερό Ctrl
pygame.K_RCTRL        # Δεξί Ctrl
pygame.K_TAB          # Tab
pygame.K_BACKSPACE    # Backspace
pygame.K_DELETE       # Delete
```

## 📊 Game Mechanics

### Scoring System

| Ενέργεια | Πόντοι |
|---------|--------|
| 1 σειρά | 100 |
| 2 σειρές | 300 |
| 3 σειρές | 500 |
| 4 σειρές | 800 |
| Hard drop | 2 per cell |

### Difficulty

Η δυσκολία αυξάνεται αυτόματα καθώς ολοκληρώνετε γραμμές. Η ταχύτητα πτώσης αυξάνεται κατά 0.02 blocks/sec για κάθε σειρά.

## � Τι είναι το Virtual Environment;

Το **virtual environment** είναι ένας απομονωμένος Python interpreter για το project σας.

### Γιατί είναι Σημαντικό;

| Χωρίς Virtual Env | Με Virtual Env |
|------------------|-----------------|
| ❌ Όλα τα packages στο global Python | ✅ Packages απομονωμένα ανά project |
| ❌ Πιθανές συγκρούσεις εκδόσεων | ✅ Πλήρης έλεγχος εκδόσεων |
| ❌ Ενοχληθείτε ολόκληρο το σύστημα | ✅ Ασφαλές και καθαρό |

### Δομή Directories

Μετά τη δημιουργία virtual environment:

```
Tetris/
├── venv/                    # Virtual environment (δημιουργείται αυτόματα)
│   ├── Scripts/ (Windows)   # Ενεργοποίηση scripts
│   │   └── Activate.ps1
│   ├── bin/ (Linux/WSL)     # Ενεργοποίηση scripts
│   │   └── activate
│   ├── lib/                 # Installed packages
│   └── pyvenv.cfg
├── main.py
├── game.py
├── pieces.py
├── renderer.py
├── constants.py
├── requirements.txt
└── README.md
```

### Πώς Δουλεύει;

1. **Δημιουργία:** `python -m venv venv` ↓ δημιουργεί τον κατάλογο `venv`
2. **Ενεργοποίηση:** Τρέχετε το script `Activate` ↓ "ενεργοποιείτε" το environment
3. **Εγκατάσταση:** Τα packages εγκαθίστανται στον `venv/lib`, όχι global
4. **Απενεργοποίηση:** `deactivate` ↓ επανέρχεστε στο global Python

## Troubleshooting

### Quick Tips

#### Πρόβλημα: "Πώς θα ξεκινήσω το παιχνίδι εύκολα;"
**Λύση:** 
- **Windows:** Δίνει διπλοκλικ στο `run_tetris.bat`
- **WSL/Linux:** Τρέξτε `bash run_tetris.sh`

Αυτά τα scripts κάνουν όλα αυτόματα (venv, dependencies, εκτέλεση)!

### Virtual Environment Issues

#### Πρόβλημα: Windows PowerShell - "Cannot be loaded because running scripts is disabled"
**Λύση:** 
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Στη συνέχεια ενεργοποιήστε το virtual environment ξανά.

#### Πρόβλημα: WSL - "command not found: venv" ή "Δημιουργία virtual environment failed"
**Λύση:**
```bash
# Εγκαταστήστε τα απαραίτητα πακέτα
sudo apt update
sudo apt install python3-full python3-venv -y

# Στη συνέχεια δοκιμάστε:
python3 -m venv venv
source venv/bin/activate
```

#### Πρόβλημα: WSL - "error: externally-managed-environment"
**Λύση:** Αυτό συμβαίνει σε Debian-based distros με Python 3.12+. Δύο επιλογές:

**Επιλογή 1 (Προτεινόμενη):** Χρησιμοποιήστε το virtual environment (αυτό κάνει το script):
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Επιλογή 2:** Override αν ξέρετε τι κάνετε:
```bash
pip install --break-system-packages -r requirements.txt
```

#### Πρόβλημα: WSL - "python: command not found"
**Λύση:** Στο WSL υπάρχει μόνο `python3`, όχι `python`. Χρησιμοποιήστε:
```bash
python3 main.py
# ή αν έχετε ενεργοποιημένο το venv:
python main.py  # θα δουλέψει
```

#### Πρόβλημα: WSL - Κανένα παράθυρο δεν εμφανίζεται
**Λύση:** Το WSL χρειάζεται X11 display. Τρεις επιλογές:

1. **Εγκατάστε VcXsrv (Προτεινόμενο):**
   - Κατεβάστε από: https://sourceforge.net/projects/vcxsrv/
   - Ανοίξτε το VcXsrv ΠΡΙΝ τρέξετε το Tetris
   - Στο WSL, προσθέστε στο `~/.bashrc`:
   ```bash
   export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0
   ```

2. **Χρησιμοποιήστε native Windows Python (Ευκολότερο):**
   - Κλείστε WSL
   - Τρέξτε από PowerShell: `.\run_tetris.bat`

3. **Χρησιμοποιήστε WSL2 με Wayland:**
   - Ενημερώστε στο WSL2
   - Εγκαταστήστε Wayland display manager

#### Πρόβλημα: "No module named pygame" ακόμα και ενεργοποιημένο το venv
**Λύση:**
1. Βεβαιωθείτε ότι το venv είναι ενεργοποιημένο (ή θα δείτε `(venv)`)
2. Τρέξτε ξανά: `pip install -r requirements.txt`

#### Πρόβλημα: Θέλω να διαγράψω το virtual environment και να το ξαναδημιουργήσω
**Λύση:**
```powershell
# Windows
Remove-Item -Recurse venv

# WSL/Linux
rm -rf venv
```
Στη συνέχεια δημιουργήστε νέο: `python -m venv venv`

### Pygame & Graphics Issues
### Pygame & Graphics Issues

### Πρόβλημα: "No module named pygame"
**Λύση:** 
1. Ενεργοποιήστε το virtual environment
2. Εγκαταστήστε το pygame:
```powershell
pip install pygame==2.5.2
```

### Πρόβλημα: Κανένα παράθυρο δεν εμφανίζεται
**Λύση:** 
- Βεβαιωθείτε ότι χρησιμοποιείτε native Windows Python (όχι WSL)
- Ή ρυθμίστε X11 forwarding αν χρησιμοποιείτε WSL
- Ή χρησιμοποιήστε το native Windows Python αντί WSL

### Πρόβλημα: Το παιχνίδι τρέχει αργά
**Λύση:** 
- Κλείστε άλλες εφαρμογές
- Η ταχύτητα πτώσης αυξάνεται με τις cleared lines (αυτό είναι κανονικό)

## 💡 Πρόσθετες Δυνατότητες

Μπορούν εύκολα να προστεθούν:
- Sound effects
- High score table
- Difficulty levels
- Themes/skins
- Multiplayer

## 📦 Dependencies

- **pygame==2.5.2** - Για γραφικά και input handling

## 📄 Άδεια

Αυτό το project είναι δημιουργημένο για εκπαιδευτικούς σκοπούς.

---

**Ευχαρίστω που παίζετε το Tetris!**
