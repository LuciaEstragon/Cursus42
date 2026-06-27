#!/usr/bin/env python3
"""
loading.py - Data analysis program using pandas, numpy, matplotlib.
Handles missing dependencies gracefully and compares pip vs Poetry.
"""

import sys
from typing import Dict, Optional, Tuple

# Type alias for module versions
VersionDict = Dict[str, Optional[str]]


def check_dependencies() -> Tuple[bool, VersionDict]:
    """
    Try to import required libraries and return their versions.

    Returns:
        (all_ok, {module_name: version or None})
    """
    modules = ['pandas', 'numpy', 'matplotlib']
    versions: VersionDict = {}
    all_ok = True

    for mod_name in modules:
        try:
            mod = __import__(mod_name)
            version = getattr(mod, '__version__', 'unknown')
            versions[mod_name] = version
            print(f"[OK] {mod_name} ({version}) - Ready")
        except ImportError:
            versions[mod_name] = None
            all_ok = False
            print(f"[FAIL] {mod_name} - Missing")

    return all_ok, versions


def show_installation_instructions() -> None:
    """Print instructions to install missing dependencies."""
    print("\nDEPENDENCIES MISSING!")
    print("Install required packages using pip or Poetry:\n")
    print("Using pip:")
    print("    pip install -r requirements.txt\n")
    print("Using Poetry:")
    print("    poetry install")
    print("    poetry run python loading.py\n")
    print("After installation, run this program again.")


def compare_pip_poetry() -> None:
    """Print differences between pip and Poetry dependency management."""
    print("\n=== Package Management Comparison ===")
    print("pip:")
    print("  - Uses requirements.txt for dependencies")
    print("  - Manual dependency resolution")
    print("  - No lockfile by default (use pip freeze > requirements.txt)")
    print("  - Global or virtual environment installs")
    print("\nPoetry:")
    print("  - Uses pyproject.toml for configuration")
    print("  - Automatic dependency resolution and locking (poetry.lock)")
    print("  - Built-in virtual environment management")
    print("  - Deterministic installs across environments")
    print("=====================================\n")


def generate_matrix_data(n_points: int = 1000):
    """Generate simulated Matrix data using numpy."""
    import numpy as np
    # Simulate signal data: a sine wave + noise
    x = np.linspace(0, 4 * np.pi, n_points)
    signal = np.sin(x) + 0.3 * np.random.randn(n_points)
    return x, signal


def analyze_and_plot() -> None:
    """Run analysis and create visualization."""
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    # Generate data
    x, signal = generate_matrix_data(1000)

    # Create DataFrame
    df = pd.DataFrame({'time': x, 'signal': signal})
    df['smoothed'] = df['signal'].rolling(window=20, min_periods=1).mean()

    # Basic statistics
    mean = np.mean(signal)
    std = np.std(signal)
    print(f"Signal statistics: mean = {mean:.4f}, std = {std:.4f}")

    print("Generating visualization...")
    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(df['time'], df['signal'], alpha=0.5, label='Raw signal (noisy)')
    plt.plot(df['time'], df['smoothed'], 'r-', linewidth=2, label='Smoothed (rolling mean)')
    plt.title('Matrix Data Analysis')
    plt.xlabel('Time')
    plt.ylabel('Signal Amplitude')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    output_file = 'matrix_analysis.png'
    plt.savefig(output_file, dpi=100)
    plt.close()
    print(f"\nAnalysis complete! Results saved to: {output_file}")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    deps_ok, versions = check_dependencies()

    if not deps_ok:
        show_installation_instructions()
        sys.exit(1)

    # All dependencies present, continue
    print("\nAll dependencies satisfied.\n")

    # Show comparison between pip and Poetry
    compare_pip_poetry()

    # Perform analysis and plotting
    try:
        analyze_and_plot()
    except Exception as e:
        print(f"Error during analysis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
