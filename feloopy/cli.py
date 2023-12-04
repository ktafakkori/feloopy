import sys
import argparse
from .clitools import detect_package_manager

__version__ = "0.2.8"

def main():
    
    parser = argparse.ArgumentParser(description="FelooPy's command-line tool")
    parser.add_argument("--detect", action="store_true", help="Detect the package manager")
    parser.add_argument("--version", action="store_true", help="Display the version of feloopy")

    args = parser.parse_args()

    if args.detect:
        detect_package_manager(verbose=True)
        
    elif args.version:
        print(f"FelooPy (v{__version__})")
        
    else:
        print("No valid command provided. Use --detect or --version.")