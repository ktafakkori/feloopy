import os
import argparse
import getpass

try:
    import tkinter as tk
    from tkinter import filedialog
except:
    ""

import nbformat
import shutil
import zipfile

from .clitools.utils import *
from .clitools import detect_package_manager


def main():
    parser = argparse.ArgumentParser(description="FelooPy's command-line tool")

    parser.add_argument("command", choices=["detect", "version", "project", "backup", "recover", "build"], help="Command to execute")

    parser.add_argument("--name", help="Name of the optimization project")

    args = parser.parse_args()

    if args.command == "detect":
        cli_detect()
    elif args.command == "version":
        cli_version()
    elif args.command == "project":
        if not args.name:
            print("Error: --name is required for the 'project' command.")
            return
        cli_project(args)
    elif args.command == "backup":
        zip_project()
    elif args.command == "recover":
        recover_project()
    elif args.command == "build":
        build_project()
    else:
        print("Invalid command. Use 'detect', 'version', 'project', 'backup', 'recover', or 'build'.")
        
if __name__ == "__main__":
    main()