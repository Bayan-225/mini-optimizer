import os
import shutil
import psutil
import platform
import ctypes
from tkinter import *
from tkinter import messagebox, ttk

def clear_temp():
    temp_paths = [
        os.getenv("TEMP"),
        r"C:\Windows\Temp",
        r"C:\Windows\Prefetch",
    ]
    deleted = 0
    for path in temp_paths:
        if not os.path.exists(path):
            continue
        for root, dirs, files in os.walk(path):
            for name in files:
                try:
                    os.remove(os.path.join(root, name))
                    deleted += 1
                except: continue
            for name in dirs:
                try:
                    shutil.rmtree(os.path.join(root, name), ignore_errors=True)
                except: continue
    messagebox.showinfo("Очистка", f"Удалено ~{deleted} файлов.")

def clear_recycle_bin():
    try:
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 0x00000001)
        messagebox.showinfo("Корзина", "Корзина очищена.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось очистить корзину: {e}")

def show_stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")
    win_ver = platform.version()
    info = (
        f"Система: Windows {win_ver}\n"
        f"CPU: {cpu}%\n"
        f"RAM: {ram.used // (1024**2)} / {ram.total // (1024**2)} MB\n"
        f"Диск: {disk.free // (1024**3)} GB свободно"
    )
    messagebox.showinfo("Состояние системы", info)



root = Tk()
root.title("Windows Optimizer")
root.geometry("310x240")
root.resizable(False, False)

style = ttk.Style(root)
style.theme_use("clam")

frame = ttk.Frame(root, padding=15)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Оптимизация системы", font=("Segoe UI", 13, "bold")).pack(pady=10)

ttk.Button(frame, text="Очистить временные файлы", command=clear_temp).pack(pady=5, fill="x")
ttk.Button(frame, text="Очистить корзину", command=clear_recycle_bin).pack(pady=5, fill="x")
ttk.Button(frame, text="Показать статистику", command=show_stats).pack(pady=5, fill="x")

ttk.Label(frame, text="by Yaroslav | Python", font=("Segoe UI", 8)).pack(side="bottom", pady=10)

root.mainloop()
