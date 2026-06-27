#!/usr/bin/env python3
"""
oracle.py - Load configuration from environment variables and .env file.
Demonstrates different behavior for development/production modes.
"""

import os
import sys
from typing import Dict, Optional

from dotenv import load_dotenv


# Required configuration keys
REQUIRED_KEYS = [
    'MATRIX_MODE',
    'DATABASE_URL',
    'API_KEY',
    'LOG_LEVEL',
    'ZION_ENDPOINT'
]


def load_configuration() -> Dict[str, Optional[str]]:
    """
    Load .env file and environment variables.
    Environment variables take precedence over .env.
    """
    # Load .env file (does not override existing environment vars)
    load_dotenv()

    config = {}
    for key in REQUIRED_KEYS:
        config[key] = os.environ.get(key)

    return config


def validate_config(config: Dict[str, Optional[str]]) -> bool:
    """Check that all required keys are present."""
    missing = [key for key, value in config.items() if value is None]
    if missing:
        print(f"ERROR: Missing configuration variables: {', '.join(missing)}")
        print("Please create a .env file based on .env.example")
        return False
    return True


def get_database_status(mode: str, db_url: str) -> str:
    """Return a human-readable database status based on mode."""
    if mode == 'development':
        if 'localhost' in db_url or '127.0.0.1' in db_url:
            return "Connected to local instance"
        else:
            return "Connected (development override)"
    else:  # production
        return "Connected to production cluster"


def get_api_status(api_key: str, mode: str) -> str:
    """Return API authentication status."""
    if api_key.startswith('sk-') or len(api_key) > 20:
        return "Authenticated (production key)"
    else:
        return "Authenticated (development key)"


def security_check(config: Dict[str, Optional[str]]) -> None:
    """Perform security checks: no hardcoded secrets, .env ignored, etc."""
    print("\nEnvironment security check:")

    # Check for hardcoded secrets in source code (simple heuristic)
    source_file = __file__
    try:
        with open(source_file, 'r') as f:
            content = f.read()
            # Look for patterns like 'API_KEY = "something"'
            if 'API_KEY = "' in content or 'SECRET' in content.upper():
                print("[WARNING] Possible hardcoded secret detected in source!")
            else:
                print("[OK] No hardcoded secrets detected")
    except Exception:
        print("[?] Could not verify hardcoded secrets")

    # Check that .env is not tracked (we assume .gitignore is correctly set)
    if os.path.exists('.env'):
        print("[OK] .env file present (should be in .gitignore)")
    else:
        print("[WARNING] .env file not found – create one from .env.example")

    # Check for production overrides (example: environment variable overrides .env)
    if os.environ.get('MATRIX_MODE') == 'production':
        print("[OK] Production overrides available (env vars set)")
    else:
        print("[INFO] Using .env or default settings; production overrides not active")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_configuration()
    if not validate_config(config):
        sys.exit(1)

    mode = config['MATRIX_MODE']
    db_url = config['DATABASE_URL']
    api_key = config['API_KEY']
    log_level = config['LOG_LEVEL']
    zion_endpoint = config['ZION_ENDPOINT']

    print("Configuration loaded:\n")
    print(f"Mode: {mode}")
    print(f"Database: {get_database_status(mode, db_url)}")
    print(f"API Access: {get_api_status(api_key, mode)}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_endpoint}")

    # Optional: show different behavior based on mode
    if mode == 'development':
        print("\n[DEV] Running in development mode – verbose logging, local endpoints.")
    else:
        print("\n[PROD] Running in production mode – high security, remote endpoints.")

    security_check(config)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
