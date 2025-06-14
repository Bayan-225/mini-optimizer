import os
import shutil
import psutil
import platform
import ctypes
from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime

LOG_FILE = "cleanup_log.txt"

CLEAN_PATHS = {
    "TEMP": os.getenv("TEMP"),
    "System Temp": os.path.join(os.getenv("SystemRoot"), "Temp"),
    "User Temp": os.path.join(os.getenv("USERPROFILE"), "AppData", "Local", "Temp"),
    "Browser Cache": os.path.join(os.getenv("USERPROFILE"), "AppData", "Local", "Microsoft", "Windows", "INetCache"),
    "Crash Dumps": os.path.join(os.getenv("USERPROFILE"), "AppData", "Local", "CrashDumps"),
    "Recycle Bin": os.path.join(os.getenv("SystemDrive") + "\\", "$Recycle.Bin"),
    "Prefetch": os.path.join(os.getenv("SystemRoot"), "Prefetch"),
    "WER": os.path.join(os.getenv("USERPROFILE"), "AppData", "Local", "Microsoft", "Windows", "WER"),
    "Packages": os.path.join(os.getenv("USERPROFILE"), "AppData", "Local", "Packages")
}

def log_deletion(filepath):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — {filepath}\n")

def clear_selected(paths):
    deleted = 0
    for name, path in paths.items():
        if not path or not os.path.exists(path):
            continue
        for root, dirs, files in os.walk(path, topdown=False):
            for fname in files:
                try:
                    fpath = os.path.join(root, fname)
                    os.remove(fpath)
                    deleted += 1
                    log_deletion(fpath)
                except:
                    continue
            for dname in dirs:
                try:
                    dpath = os.path.join(root, dname)
                    shutil.rmtree(dpath, ignore_errors=True)
                except:
                    continue
    messagebox.showinfo("Cleaning", f"Deleted ~{deleted} files. Information in {LOG_FILE}")

def clear_recycle_bin():
    try:
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0x00000001)
        messagebox.showinfo("Recycle", "Recycle cleaned.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to empty recycle: {e}")

def show_stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")
    win_ver = platform.version()
    info = (
        f"System: Windows {win_ver}\n"
        f"CPU: {cpu}%\n"
        f"RAM: {ram.used // (1024**2)} / {ram.total // (1024**2)} MB\n"
        f"Disk: {disk.free // (1024**3)} GB free"
    )
    messagebox.showinfo("System Status", info)

# GUI
root = Tk()
root.title("Windows Optimizer")
root.geometry("340x400")
root.resizable(False, False)

style = ttk.Style(root)
style.theme_use("clam")

frame = ttk.Frame(root, padding=15)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="System optimization", font=("Segoe UI", 13, "bold")).pack(pady=10)

# Checkboxes
check_vars = {}
for name in CLEAN_PATHS:
    var = BooleanVar(value=True)
    chk = ttk.Checkbutton(frame, text=name, variable=var)
    chk.pack(anchor="w")
    check_vars[name] = var

def run_cleanup():
    selected = {name: CLEAN_PATHS[name] for name in check_vars if check_vars[name].get()}
    clear_selected(selected)

ttk.Button(frame, text="Clear selected", command=run_cleanup).pack(pady=10, fill="x")
ttk.Button(frame, text="Clear recycle", command=clear_recycle_bin).pack(pady=5, fill="x")
ttk.Button(frame, text="Show statistics", command=show_stats).pack(pady=5, fill="x")

ttk.Label(frame, text="by Yaroslav | Python", font=("Segoe UI", 8)).pack(side="bottom", pady=10)

root.mainloop()
