# Mini Optimizer

**Mini Optimizer** — это простое GUI-приложение для Windows, написанное на Python, которое позволяет:

- Очистить временные файлы и кэш
- Очистить корзину
- Показать статистику системы (CPU, RAM, Disk)
- Выбрать, какие директории очищать
- Сохранять лог удалённых файлов

## Скачать

[Скачать последнюю версию (.zip)](https://github.com/Bayan-225/mini-optimizer/releases/latest)

## Требования

- Windows 10/11
- Python 3.10+ (если не используешь `.exe`)
- Не требует установки, просто запускай `mini_optimizer.exe`

## Сборка самостоятельно

Если хочешь собрать самостоятельно:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed mini_optimizer.py
