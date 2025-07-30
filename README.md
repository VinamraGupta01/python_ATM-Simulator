# 💳 ATM SIMULATOR — PYTHON CONSOLE PROJECT

A beginner-friendly **ATM simulator** built using pure Python. This console-based application replicates basic ATM functionalities such as **balance inquiry**, **cash withdrawal**, **deposit**, and **PIN verification** — all wrapped in a simple and interactive CLI menu.

---

## 🛠️ FEATURES

- 🔐 Secure PIN-based login system  
- 💵 Withdraw, deposit, and check account balance  
- 🔁 Continuous menu loop until user exits  
- ⚠️ Input validation with friendly error handling  
- ❌ Safe and clean exit confirmation  
- 🐍 Built using **pure Python** – no external dependencies  

---

## ▶️ HOW TO RUN

```bash
python atm.py
````

Make sure you have Python 3.x installed. You can download Python from [python.org](https://www.python.org/).

---

## 📁 PROJECT STRUCTURE

| File Name   | Description                                                             |
| ----------- | ----------------------------------------------------------------------- |
| `atm.py`    | Main script that runs the console-based ATM simulator                   |
| `atm.ico`   | Optional custom icon for executable branding                            |
| `setup.py`  | Installer builder script (Windows `.msi`) using distutils (`bdist_msi`) |
| `README.md` | Project documentation                                                   |

---

## 🧪 EXAMPLE QUESTIONS

```
Welcome to ATM

Enter your 4-digit PIN: ****

1. Balance Inquiry
2. Deposit Money
3. Withdraw Money
4. Exit

Choose an option: _
```

---

## 🛠️ CREATE EXECUTABLE (.exe)

To convert this project into a Windows executable:

```bash
pyinstaller --onefile atm.py
```

> *(Ensure `pyinstaller` is installed using `pip install pyinstaller`)*

---

## 📦 BUILD INSTALLER (MSI - Optional)

Use the provided `setup.py` to generate a Windows installer:

```bash
python setup.py bdist_msi
```

---

## 📄 LICENSE

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 🌟 LIKE THIS PROJECT?

If you found this helpful or educational, please ⭐ star the repository — it motivates further development!

---

## 👤 AUTHOR

**Vinamra Gupta**
📧 (gvinamra73@gmail.com)
🔗 (www.linkedin.com/in/vinamra-gupta-0aa4b4375)

```

