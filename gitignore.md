# =========================
# 🔹 EyeLink / Experiment Builder
# =========================

# Compiled experiment output
experiment/compiled/
bin/
Release/
Debug/

# EyeLink data (NEVER upload)
*.edf
*.asc

# Behavioral output (can be large / sensitive)
data/raw/
*.dat

# =========================
# 🔹 Stimuli (if confidential)
# =========================

stimuli/audio/
stimuli/raw/

# =========================
# 🔹 Python
# =========================

__pycache__/
*.pyc
*.pyo
*.pyd

# Virtual environments
venv/
.env/
.venv/

# Jupyter
.ipynb_checkpoints/

# =========================
# 🔹 Data processing outputs
# =========================

data/processed/
*.csv

# (Optional: keep only sample data)
!data/sample/
!data/sample/*.csv

# =========================
# 🔹 OS / System files
# =========================

.DS_Store
Thumbs.db
desktop.ini

# =========================
# 🔹 IDEs / Editors
# =========================

.vscode/
.idea/

# =========================
# 🔹 Logs / temp
# =========================

*.log
*.tmp
*.bak

# =========================
# 🔹 Misc
# =========================

*.zip
*.rar
*.7z
