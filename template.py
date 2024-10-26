import os                 # Imports the os module for interacting with the operating system, such as creating directories.
from pathlib import Path   # Imports the Path class from pathlib module to handle file paths in a cross-platform way.
import logging             # Imports the logging module to set up logging for tracking and debugging.

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')  
# Configures the logging to display messages at the INFO level or higher.
# The format includes a timestamp and the message, making it useful for tracking events as they happen.

project_name = 'textSummarizer'  
# Sets the project name, which will be used as a directory name and base for other file paths.
# This allows reusability if the project name changes.

list_of_files = [              # Initializes a list to hold all the file paths required for the project structure.
    ".github/workflows/.gitkeep",   # Placeholder file for GitHub Actions workflows; ensures empty directories are committed to Git.
    f"src/{project_name}/__init__.py",  # __init__.py file to make 'src/textSummarizer' a Python package.
    f"src/{project_name}/components/__init__.py",  # __init__.py for 'components' package, where modules can be added.
    f"src/{project_name}/utils/__init__.py",  # __init__.py for 'utils' package, typically for utility functions.
    f"src/{project_name}/utils/common.py",  # common.py file to store general utility functions for the project.
    f"src/{project_name}/logging/__init__.py",  # __init__.py for 'logging' package to manage logging for the project.
    f"src/{project_name}/config/__init__.py",  # __init__.py for 'config' package to manage configuration settings.
    f"src/{project_name}/config/configuration.py",  # configuration.py to handle project configuration details.
    f"src/{project_name}/pipeline/__init__.py",  # __init__.py for 'pipeline' package, where the processing pipeline can be added.
    f"src/{project_name}/entity/__init__.py",  # __init__.py for 'entity' package, typically for defining data structures or models.
    f"src/{project_name}/constants/__init__.py",  # __init__.py for 'constants' package to store project constants.
    "config/config.yaml",  # Main configuration file in YAML format to define configurations for the project.
    "params.yaml",  # Separate YAML file to specify parameters for the project, useful for hyperparameters or settings.
    "app.py",  # Main app script for the project, likely the entry point for the web app or core application.
    "main.py",  # Another main script, often for CLI or different app entry points.
    "Dockerfile",  # Dockerfile for building a Docker image, specifying dependencies and environment setup for deployment.
    "requirements.txt",  # File listing all Python dependencies needed for the project.
    "setup.py",  # Script for setting up the project as an installable package.
    "research/trials.ipynb"  # Jupyter notebook for experimenting with different models and trials, placed in a research directory.
]


for filepath in list_of_files:  # Iterates over each file path in the list_of_files list.
    filepath = Path(filepath)   # Converts the string path into a Path object, making it easier to work with.
    filedir, filename = os.path.split(filepath)  # Splits the file path into its directory and filename components.

    if filedir != "":  # Checks if the file has a directory component (not just a filename).
        os.makedirs(filedir, exist_ok=True)  # Creates the directory if it doesn't exist, using 'exist_ok=True' to avoid errors if it already exists.
        logging.info(f"Creating directory: {filedir} for file: {filename}")  # Logs a message indicating the directory creation.        

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  # Checks if the file doesn't exist or is empty (size is 0).
        with open(filepath, "w") as f:                                      # Opens the file in write mode ('w') and creates it if it doesn't exist.
            pass                                                            # The 'pass' statement does nothing, effectively creating an empty file.
            logging.info(f"Creating empty file: {filepath}")                # Logs a message indicating the creation of an empty file.

    else:
        logging.info(f"{filename} already exists")                          # Logs a message if the file already exists, indicating it's not being created again.


