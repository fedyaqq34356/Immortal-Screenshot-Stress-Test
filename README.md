<div align="center">

# 🖥️ Immortal Screenshot + Stress Test

**A lightweight Windows utility that automatically captures screenshots at regular intervals
and runs continuous maximum-load stress tests on CPU and RAM.**

<br>

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078d4?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-GPL%20v3-blue?style=for-the-badge&logo=gnu&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 📁 **Daily Folder Organization** | Automatically creates a new folder named `YYYY-MM-DD` inside each selected directory |
| 📸 **Automated Screenshots** | Captures full-screen screenshots every 30 seconds — saved as timestamped `.png` files |
| 📝 **Companion Text Files** | Creates a matching `.txt` file containing the word `immortal` alongside each screenshot |
| 🔥 **CPU Stress Test** | Runs infinite calculations across all logical cores simultaneously |
| 💾 **RAM Stress Test** | Continuously allocates 50 MB blocks without freeing them — true crash-test mode |
| 🪟 **Minimal GUI** | Folder selection via standard Windows dialog — no complex configuration required |

---

## 🚀 Quick Start

**1. Make sure you have Python 3.8 or newer installed.**

**2. Install the required packages:**

```cmd
pip install mss pillow schedule
```

**3. Place all files in the same folder:**

```
📂 Project
 ├── main.py
 ├── screenshot.py
 ├── stress_cpu.py
 ├── stress_ram.py
 └── error_handler.py
```

**4. Launch it:**

```cmd
python main.py
```

Or simply **double-click** `main.py` in Explorer.

**5. Select one or more folders** using the dialog window.

The program starts immediately and runs silently in the background. ✅

---

## ⚙️ Configuration

Open `screenshot.py` and edit these variables at the top of the file:

```python
INTERVAL_SECONDS = 30   # How often to take a screenshot (in seconds)
```

---

## 🗂️ Output Structure

```
📂 Selected Folder
 └── 📂 2025-06-15
      ├── 2025-06-15_14-00-00.png
      ├── 2025-06-15_14-00-00.txt
      ├── 2025-06-15_14-00-30.png
      ├── 2025-06-15_14-00-30.txt
      ├── 2025-06-15_14-01-00.png
      └── 2025-06-15_14-01-00.txt
```

---

## 📌 Autostart with Windows

**1.** Create a file named `start.bat` in the same folder as the scripts:

```bat
@echo off
python "C:\Full\Path\To\main.py"
```

**2.** Press `Win + R`, type `shell:startup`, and press Enter.

**3.** Move or shortcut `start.bat` into that folder.

The tool will now launch automatically every time Windows starts.

---

## ⚠️ Warning

> **This tool is a genuine crash-test utility.**
>
> The RAM stress test continuously allocates memory **without any limit**.
> This may cause system slowdown, freezing, or force other applications to close.
>
> ⚡ Use **only for testing purposes** on a dedicated or disposable machine.

---

## 📦 Dependencies

```
mss        — fast cross-platform screenshot capture
Pillow     — image processing
schedule   — task scheduling
```

Install all at once:

```cmd
pip install mss pillow schedule
```

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0**.  
See the [LICENSE](LICENSE) file for full details, or read it at [gnu.org/licenses/gpl-3.0](https://www.gnu.org/licenses/gpl-3.0).

---

<div align="center">

**Made with ❤️, just for fun**

If you find this useful, please consider giving it a ⭐ — it means a lot!

</div>