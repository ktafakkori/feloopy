# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

import argparse

try:
    import tkinter as tk
    from tkinter import filedialog
except:
    pass

from .clitools import *

def cli_detect():
    detect_package_manager(verbose=True)

def main():
    parser = argparse.ArgumentParser(description="FelooPy's command-line tool")

    parser.add_argument("--name", nargs='?', const=None, help="Name of the optimization project")
    parser.add_argument("--version", action="store_true", help="Print the version of FelooPy")
    parser.add_argument("-version", action="store_true", help="Print the version of FelooPy")
    parser.add_argument("command", nargs='?', default=None, help="Command to execute")
    parser.add_argument("file", nargs='?', default=None, help="Python file to run (for 'run' command)")
    parser.add_argument("package", nargs='?', default=None, help="Python package to install (for 'install' command)")
    parser.add_argument("extension", nargs='+', default=[], help="VS Code extension(s) to install")

    args = parser.parse_args()

    command_functions = {
        "detect": cli_detect,
        "project": lambda: cli_project(args) if args.name else parser.error("--name is required for the 'project' command."),
        "extension": lambda: install_vscode_extensions(args.extension) if args.extension else print("Extensions to install: []."),
        "backup": zip_project,
        "recover": recover_project,
        "build": build_project,
        "clean": clean_project,
        "deps": get_installed_dependencies,
        "run": lambda: run_project(args.file) if args.file else print("Error: Please specify a Python file to run."),
        "install": lambda: pip_install(args.package or args.name) if args.package or args.name else None,
    }
    
    if args.version:
        cli_version()
    elif args.command in command_functions.keys():
        command_functions[args.command]()
    else:
        print("Invalid command.")
        
if __name__ == "__main__":
    main()