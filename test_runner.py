import os
import sys
import unittest

def discover_and_run_tests():
    # Get the current directory of the script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Find all files with the name 'main.py' in subdirectories
    test_modules = [
        os.path.join(root, 'main.py')
        for root, dirs, files in os.walk(current_directory)
        if 'main.py' in files
    ]

    # Import and run each test module
    for test_module in test_modules:
        # Get the directory of the test module
        test_module_directory = os.path.dirname(test_module)

        # Add the test module directory to sys.path
        sys.path.append(test_module_directory)

        # Import the main module (assuming it has a unittest.TestLoader)
        module_name = os.path.basename(test_module_directory)
        try:
            module = __import__(module_name)
        except Exception as e:
            print(f"Error importing module {module_name}: {e}")
            continue

        # Run the tests
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(module)
        unittest.TextTestRunner().run(suite)

        # Remove the test module directory from sys.path
        sys.path.remove(test_module_directory)

if __name__ == "__main__":
    discover_and_run_tests()
