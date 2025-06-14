# Mini Optimizer

**Mini Optimizer** — This is a simple GUI application for Windows written in Python that allows you to:

- Clear temporary files and cache
- Clear recycle bin
- Show system statistics (CPU, RAM, Disk)
- Select which directories to clean
- Keep log of deleted files

## Download

[Download latest version (.zip)](https://github.com/Bayan-225/mini-optimizer/releases/latest)

## Requirements

- Windows 10/11
- Python 3.10+ (if you don't use `.exe`)
- No installation required, just run `mini_optimizer.exe`

## Build by yourself

If you want to build it yourself:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed mini_optimizer.py
