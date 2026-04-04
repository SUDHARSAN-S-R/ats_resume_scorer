"""
Build script to create executable for ATS Resume Analyzer
Run this script to generate the .exe file
"""
import PyInstaller.__main__
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    'app.py',
    '--name=ATS_Resume_Analyzer',
    '--onefile',
    '--windowed',
    '--add-data=templates;templates',
    '--add-data=static;static',
    '--hidden-import=fitz',
    '--hidden-import=sentence_transformers',
    '--hidden-import=sklearn.metrics.pairwise',
    '--hidden-import=sklearn.metrics',
    '--hidden-import=werkzeug',
    '--hidden-import=flask',
    '--hidden-import=webbrowser',
    '--icon=NONE',
    '--noconfirm',
])

print("\n" + "="*60)
print("Build completed!")
print("Your executable is in: dist/ATS_Resume_Analyzer.exe")
print("="*60)
