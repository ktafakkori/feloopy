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
   subparsers = parser.add_subparsers(dest="command")

   parser.add_argument("--version", action="store_true", help="Print the version of FelooPy")
   parser.add_argument("-version", action="store_true", help="Print the version of FelooPy")

   setup_parser = subparsers.add_parser("setup")
   
   project_parser = subparsers.add_parser("project")
   project_parser.add_argument("--name", nargs='?', const=None, help="Name of the optimization project")
   project_parser.add_argument('--type', nargs='?', const=None, help='Specify project type.')

   manager1_parser = subparsers.add_parser("clean")
   manager2_parser = subparsers.add_parser("backup")
   manager3_parser = subparsers.add_parser("recover")
   manager3_parser.add_argument("--name", nargs='?', const=None, help="Name of the backup")
   manager4_parser = subparsers.add_parser("build")

   script_parser = subparsers.add_parser("run")
   script_parser.add_argument("file", nargs='?')
   
   ext_parser = subparsers.add_parser("ext")
   ext_parser.add_argument("extensions", nargs='*', help="Extensions to install")

   install_parser = subparsers.add_parser("install")
   install_parser.add_argument("-u", "--update", action="store_true", help="Update installed packages to the latest versions")
   install_parser.add_argument("packages", nargs='*', help="Packages to install")

   uninstall_parser = subparsers.add_parser("uninstall")
   uninstall_parser.add_argument("packages", nargs='*', help="Packages to uninstall")

   args = parser.parse_args()


   command_functions = {
       "setup": run_setup_file,
       "detect": cli_detect,
       "project": lambda: cli_project(args) if args.name else parser.error("--name is required for the 'project' command."),
       "ext": lambda: install_vscode_extensions(args.extensions) if args.extensions is not None else print("Extensions to install: []."),
       "backup": zip_project,
       "recover": lambda: recover_project(args) if args else print("invalid command."),
       "build": build_project,
       "clean": clean_project,
       "deps": get_installed_dependencies,
       "run": lambda: run_project(args.file) if args.file else print("Error: Please specify a Python file to run."),
       "install": lambda: pip_install(args.packages, update=args.update) if args.packages else print("Error: Please specify packages to install."),
       "uninstall": lambda: pip_uninstall(args.packages) if args.packages else print("Error: Please specify packages to uninstall."),
   }

   if args.version:
       cli_version()
   elif args.command in command_functions.keys():
       command_functions[args.command]()
   else:
       print("Invalid command.")

if __name__ == "__main__":
   main()