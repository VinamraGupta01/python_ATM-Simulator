from cx_Freeze import setup, Executable
import sys

includefiles = ['atm.ico']
excludes = []
packages = []
base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

shortcut_table = [
    (
        "DesktopShortcut",
        "DesktopFolder",
        "ATM Simulator",
        "TARGETDIR",
        "[TARGETDIR]atm.exe",
        None, None, None, None, None, None,
        "TARGETDIR"
    )
]

msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {"data": msi_data}

setup(
    version="0.1",
    description="ATM Simulator",
    author="Vinamra Gupta",
    name="ATM Simulator",
    options={
        'build_exe': {
            'include_files': includefiles
        },
        'bdist_msi': bdist_msi_options
    },
    executables=[
        Executable(
            script="atm.py",
            base=base,
            icon="atm.ico"
        )
    ]
)
