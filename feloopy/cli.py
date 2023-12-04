import sys
from .clitools import detect_package_manager


def main():

    if len(sys.argv) == 2 and sys.argv[1] == "detect":
        detect_package_manager()