"""Launch: py -m streamlit run Lab18/lab18_app.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from investor_app_common import run
run(panel_mode=False)
