#!/usr/bin/env python3
"""
Test runner for the KDMeinBuch application.
"""
import os
import sys
import importlib
import unittest
from pathlib import Path

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_all_tests():
    """Run all tests in the tests directory."""
    # Get all test files
    test_files = list(Path(__file__).parent.glob("test_*.py"))
    
    if not test_files:
        print("No test files found!")
        return
    
    print(f"Found {len(test_files)} test files to run.")
    
    # Run each test file
    for test_file in test_files:
        module_name = test_file.stem
        print(f"\n--- Running tests from {module_name} ---")
        
        try:
            # Import and run the tests
            module = importlib.import_module(f"tests.{module_name}")
            
            # If the module has a main function, run it
            if hasattr(module, "__main__") and callable(module.__main__):
                module.__main__()
            # If the module has test_ functions, run them
            else:
                for name in dir(module):
                    if name.startswith("test_") and callable(getattr(module, name)):
                        print(f"Running {name}...")
                        getattr(module, name)()
        
        except Exception as e:
            print(f"Error running tests in {module_name}: {e}")


if __name__ == "__main__":
    print("=== Running KDMeinBuch Tests ===")
    run_all_tests()
    print("\n=== All tests completed ===") 