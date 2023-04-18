import ctypes
import pathlib
import sys
from buildVars import addon_info

def createSymlink(srcDir, instDir):
    if not isAdmin():
        if sys.version_info.major == 3 and sys.version_info.minor < 8:
            print("This script cannot be run on versions of python less than 3.8 without administrator privileges")
            sys.exit()
    try:
        instDir.symlink_to(srcDir, target_is_directory=True)
    except WindowsError as e:
        if e.winerror == 1314:
            print("You will need to enable developer mode on your system to run this script")

def isAdmin():
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def main():
    addonName = addon_info["addon_name"]
    srcDir = pathlib.Path().absolute() / "addon"
    instDir = pathlib.Path.home() / f"appdata/roaming/nvda/addons/{addonName}"
    if instDir.exists() and     instDir.is_symlink():
        ans = input(f"{addonName} is already installed. Do you want to remove it from NVDA?")
        if ans.lower() == "y":
            instDir.unlink()
        sys.exit()
    else:
        createSymlink(srcDir, instDir)

if __name__ == "__main__":
    main()
