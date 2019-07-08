import sys
from cx_Freeze import setup, Executable

setup(
    name="AdminTests",
    version="0.0",
    descripton="# --- #",
    executables=[Executable("runas.py")])
