# ATS Resume Analyzer - Build Instructions

## Creating the Executable

### Method 1: Using the build script (Recommended)
```powershell
py build_exe.py
```

### Method 2: Direct PyInstaller command
```powershell
pyinstaller --name=ATS_Resume_Analyzer --onefile --windowed --add-data="templates;templates" --add-data="static;static" --hidden-import=sentence_transformers --hidden-import=sklearn.metrics.pairwise --hidden-import=fitz --hidden-import=werkzeug --collect-all=sentence_transformers --collect-all=torch --collect-all=transformers --noconfirm app.py
```

### Method 3: Using spec file (Advanced)
1. First generate the spec file:
```powershell
pyi-makespec --name=ATS_Resume_Analyzer --onefile --windowed app.py
```

2. Edit the spec file if needed

3. Build from spec:
```powershell
pyinstaller ATS_Resume_Analyzer.spec
```

## Output Location
After building, your executable will be in:
- `dist/ATS_Resume_Analyzer.exe`

## Running the Executable
Simply double-click `ATS_Resume_Analyzer.exe` and it will:
1. Start the Flask server
2. Automatically open your default browser to http://127.0.0.1:5557

## Notes
- First run may be slow as it downloads the AI model (one-time only)
- The exe file will be around 500MB-1GB due to bundled dependencies
- Make sure you have enough disk space
- Antivirus software might flag the exe initially (false positive)

## Troubleshooting
If the build fails:
1. Make sure all dependencies are installed: `uv sync`
2. Try building without `--onefile` flag for faster builds
3. Check if antivirus is blocking PyInstaller
