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

    log_file_path = os.path.join(project_dir, "log.txt")
    with open(log_file_path, "w") as log_file:
        log_file.write(f"""
# log for {project_name}
# author: {get_user_name()}
# date: {get_current_date()}

# Notes, to-dos, and other information can be added here.
""")
        
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
    
    except:
        
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
    backup_dir = os.path.join(".", "backup")
    os.makedirs(backup_dir, exist_ok=True)

    current_datetime = get_current_datetime()
    zip_file_name = f"src-{current_datetime}.zip"
    zip_file_path = os.path.join(backup_dir, zip_file_name)

    all_files = [os.path.relpath(os.path.join(dp, f), start=".") for dp, dn, filenames in os.walk(".") for f in filenames + dn if "backup" not in os.path.join(dp, f)]

    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for file in all_files:
            zipf.write(file, arcname=file)

    print(f"Project excluding 'backup' directory zipped and saved at: {zip_file_path}")


def recover_project():
    src_files = get_recent_src_files()

    print("Recent src files:")
    for i, src_file in enumerate(src_files, start=1):
        print(f"{i}. {src_file}")
        
    selected_index = int(input("Enter the number of the src file to recover: ")) - 1

    if 0 <= selected_index < len(src_files):

        selected_src_file = src_files[selected_index]

        delete_all_except_backup()

        extract_src(selected_src_file)

        print(f"Project recovered from {selected_src_file}")
    else:
        print("Invalid selection.")

def get_recent_src_files():
    backup_dir = os.path.join(".", "backup")
    src_files = [f for f in os.listdir(backup_dir) if f.startswith("src-") and f.endswith(".zip")]
    src_files.sort(reverse=True)
    return src_files[:10]

def delete_all_except_backup():
    for item in os.listdir("."):
        if os.path.isdir(item) and item != "backup":
            shutil.rmtree(item)
        elif os.path.isfile(item) and item != "backup":
            os.remove(item)

def extract_src(src_file):
    backup_dir = os.path.join(".", "backup")
    zip_file_path = os.path.join(backup_dir, src_file)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(".")
        
def get_current_datetime():
    from datetime import datetime
    return datetime.now().strftime("on-%Y-%m-%d-at-%H-%M-%S")


def build_project():

    backup_dir = os.path.join(".", "backup")
    os.makedirs(backup_dir, exist_ok=True)

    venv_name = input("Enter the name of the virtual environment (venv): ")

    if not venv_name:
        print("Error: Virtual environment (venv) name is required.")
        return

    venv_dir = os.path.abspath(os.path.join('..', venv_name))

    if not os.path.exists(venv_dir):
        print(f"Error: Virtual environment (venv) directory '{venv_dir}' not found.")
        return

    project_venv_dir = os.path.join(".", venv_name)

    shutil.copytree(venv_dir, project_venv_dir, symlinks=True, ignore=shutil.ignore_patterns('*.pyc', '__pycache__'))

    current_datetime = get_current_datetime()
    zip_file_name = f"build-{current_datetime}.zip"
    zip_file_path = os.path.join(backup_dir, zip_file_name)

    all_files = [os.path.relpath(os.path.join(dp, f), start=".") for dp, dn, filenames in os.walk(".") for f in filenames + dn if "backup" not in os.path.join(dp, f)]

    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for file in all_files:
            zipf.write(file, arcname=file)

    build_dir_name = f"build"
    build_dir_path = os.path.join(".", build_dir_name)
    os.makedirs(build_dir_path, exist_ok=True)

    build_zip_file_path = os.path.join(build_dir_path, zip_file_name)
    shutil.move(zip_file_path, build_zip_file_path)

    print(f"Project including '{venv_name}' directory built and saved at: {build_zip_file_path}")