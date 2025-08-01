# 📦 Backup Script - Python

This repository contains a Python script `backup.py` that performs safe file backups from a source directory to a destination directory.

## 🧠 Objective

To ensure critical files are regularly backed up by copying all files from a source directory to a destination directory while:

- Preventing filename collisions by appending timestamps.
- Gracefully handling missing directories or other errors.

## 🛠️ How It Works

- The script takes **two arguments**:

  1. `source directory`
  2. `destination directory`
- It checks whether the destination folder already contains a file with the same name.

  - If **not**, it copies the file directly.
  - If **yes**, it appends a current timestamp to the file name before copying.

## ✅ Requirements

- Python 3.x

No external libraries are required.

## 🚀 Usage

Run the script using the following command:

```bash
python backup.py /path/to/source /path/to/destination
```
