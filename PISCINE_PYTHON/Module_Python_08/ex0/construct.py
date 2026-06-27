#!/usr/bin/env python3
"""
construct.py - Detect if running inside a virtual environment and display
environment information.
"""

import os
import sys
import site
from typing import Tuple, Optional


def get_venv_status() -> Tuple[bool, Optional[str], Optional[str]]:
    """
    Determine if the script is running inside a virtual environment.

    Returns:
        Tuple (is_venv, venv_name, venv_path)
    """
    # Standard check for Python 3.3+
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )
    # Also check VIRTUAL_ENV environment variable
    venv_env = os.environ.get('VIRTUAL_ENV')
    if venv_env and not in_venv:
        in_venv = True

    if in_venv:
        venv_path = sys.prefix
        if venv_env:
            venv_name = os.path.basename(venv_env)
        else:
            venv_name = os.path.basename(venv_path)
        return True, venv_name, venv_path
    else:
        return False, None, None


def get_package_path() -> str:
    """Return the site-packages directory for the current environment."""
    # site.getsitepackages() returns list of directories
    paths = site.getsitepackages()
    if paths:
        return paths[0]
    return "Unknown"


def main() -> None:
    is_venv, venv_name, venv_path = get_venv_status()
    current_python = sys.executable

    if not is_venv:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {current_python}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment! "
              "The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("    python -m venv matrix_env")
        print("    source matrix_env/bin/activate  # On Unix")
        print("    matrix_env\\Scripts\\activate     # On Windows")
        print()
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {current_python}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")
        print()
        print("SUCCESS: You're in an isolated environment! "
              "Safe to install packages without affecting the global system.")
        print(f"Package installation path: {get_package_path()}")


if __name__ == "__main__":
    main()
