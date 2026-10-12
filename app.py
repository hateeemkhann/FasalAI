"""
Fasal AI — Streamlit Entry Point Launcher
Enables running directly via: streamlit run app.py
"""
import sys
from pathlib import Path

# Add src/ to sys.path
SRC_DIR = Path(__file__).resolve().parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

# Execute src/app.py
app_path = SRC_DIR / "app.py"
with open(app_path, "r", encoding="utf-8") as f:
    code = compile(f.read(), str(app_path), "exec")
    exec(code, globals())
