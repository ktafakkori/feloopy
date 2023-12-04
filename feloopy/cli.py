import os
import argparse
import getpass
import tkinter as tk
from tkinter import filedialog
import nbformat
import shutil
import zipfile

from .clitools import detect_package_manager

__version__ = "v0.2.8"

def create_optimization_project(project_name, directory="."):

    project_dir = os.path.join(directory, project_name)

    os.makedirs(project_dir, exist_ok=True)

    subdirectories = ["data", "modules", "results"]

    for subdirectory in subdirectories:
        subdirectory_path = os.path.join(project_dir, subdirectory)
        os.makedirs(subdirectory_path, exist_ok=True)

    main_file_path = os.path.join(project_dir, "main.py")
    with open(main_file_path, "w") as main_file:
        main_file.write(f"""
# name: {project_name}
# author: {get_user_name()}
# feloopy version: {__version__}
# date: {get_current_date()}
""")

    ipynb_file_path = os.path.join(project_dir, f"debug.ipynb")
    with open(ipynb_file_path, "w") as ipynb_file:
        nb = nbformat.v4.new_notebook()
        nb['metadata'] = {
            'name:': project_name,
            'author:': get_user_name(),
            'feloopy version:': __version__,
            'date:': get_current_date()
        }
        nbformat.write(nb, ipynb_file)

    print(f"Optimization project '{project_name}' created at: {project_dir}")

def get_user_name():
    return getpass.getuser()

def get_current_date():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")

def select_directory():
    try:
        root = tk.Tk()
        root.withdraw()
        directory = filedialog.askdirectory(title="Select Project Directory")
        root.destroy()
        return directory
    except tk.TclError:
        print("Error: Unable to use graphical file dialog. Please enter the directory manually.")
        return input("Enter the project directory: ")

def cli_detect():
    detect_package_manager(verbose=True)

def cli_version():
    print(f"FelooPy ({__version__})")

def cli_project(args):
    directory = select_directory()
    if directory:
        create_optimization_project(args.name, directory)

def zip_project():
    build_dir = os.path.join(".", "build")
    os.makedirs(build_dir, exist_ok=True)

    zip_file_path = os.path.join(build_dir, "src.zip")

    all_files = [os.path.relpath(os.path.join(dp, f), start=".") for dp, dn, filenames in os.walk(".") for f in filenames + dn if "build" not in os.path.join(dp, f)]

    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for file in all_files:
            zipf.write(file, arcname=file)

    print(f"Project excluding 'build' directory zipped and saved at: {zip_file_path}")

def main():
    parser = argparse.ArgumentParser(description="FelooPy's command-line tool")

    parser.add_argument("command", choices=["detect", "version", "project", "zip"], help="Command to execute")

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
    elif args.command == "zip":
        zip_project()
    else:
        print("Invalid command. Use 'detect', 'version', 'project', or 'zip'.")

if __name__ == "__main__":
    main()