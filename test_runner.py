import subprocess
import os

if __name__ == '__main__':
    # Get the current directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Define the path to the 'tests' directory
    tests_directory = os.path.join(current_directory, 'tests')

    # List all directories in the 'tests' directory
    test_modules = [d for d in os.listdir(tests_directory) if os.path.isdir(os.path.join(tests_directory, d))]

    # Run each main.py file in the test modules
    for module in test_modules:
        main_file = os.path.join(tests_directory, module, 'main.py')
        subprocess.run(['python', main_file])
