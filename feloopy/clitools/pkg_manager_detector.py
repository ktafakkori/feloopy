import subprocess
import sys

def detect_package_manager():
    
    common_package_managers = ['apt-get', 'dnf', 'yum', 'pacman', 'zypper', 'apk']

    for cmd in common_package_managers:
        try:
            subprocess.run(['which', cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print(f"found the {cmd} package manager.")
            return cmd
        except subprocess.CalledProcessError:
            pass

    if sys.platform.startswith('win'):
        try:
            subprocess.run(['choco', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print("Found Chocolatey package manager.")
            return 'choco'
        except subprocess.CalledProcessError:
            pass

    if sys.platform.startswith('darwin'):
        try:
            subprocess.run(['brew', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print("Found Homebrew package manager.")
            return 'brew'
        except subprocess.CalledProcessError:
            pass

    print("None of the common package managers found. Exiting installation.")
    sys.exit(1)