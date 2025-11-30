# Reindeer - Python Virtual Environment Manager

[中文](README.md)

Reindeer - Python Virtual Environment Manager is a graphical tool designed to simplify the setup and management of Python projects. It aims to quickly create virtual environments and launch projects, avoiding project conflicts that occur when starting different projects. To address these issues encountered during project development, the author created this tool.

With a clean and beautiful interface, Reindeer can easily create virtual environments, manage dependencies, and execute automated project startup scripts.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey.svg)

## Features

- Automatically detect and install `uv` tool
- Create Python virtual environments using the ultra-fast `uv` tool
- Automatically install dependencies from `requirements.txt`
- Can automatically write default project entry py files
- Configurable custom package index mirror sources for fast downloading of different dependency packages
- Generate Windows batch files to activate virtual environments and quickly start projects, avoiding the need to activate virtual environments and then start projects each time
- Beautiful, modern colored graphical interface

## Requirements

- Python 3.7+
- [uv](https://github.com/astral-sh/uv) - An extremely fast Python package installer and resolver

## Installation

The following method is for members who want to study the source code. Beginners can use the compiled package provided by me.

1. Ensure the predefined environment exists
   ```
   uv venv [project name]
   ```
2. Clone or download this repository
3. Install required dependencies (if not already present in the environment):
   ```
   uv pip install -r requirements.txt
   ```

## Usage

To run the application:

1. Activate the virtual environment
2. Run the application:
   ```
   python run.py
   ```

## Application Functionality

In the graphical interface:

- Select project directory
- Configure virtual environment options
- Click "Execute Configuration" to set up the environment
- Optionally generate batch files for quick startup

### Environment Configuration Tab

- **Project Path**: Select the root directory of the Python project
- **Virtual Environment Name**: Name of the virtual environment (default is "venv")
- **Auto-install UV**: Automatically install uv if it does not exist
- **Install requirements.txt**: Install dependencies from it if present
- **Mirror Source**: Specify custom package index URL
- **Execute Script**: Python script to run after environment setup completes

### Batch File Generation Tab

- **Generate Batch File**: Create a Windows batch file that will:
  1. Activate the predefined environment
  2. Activate the project virtual environment
  3. Navigate back to the project directory
  4. Execute the specified Python script (if any)
  5. Keep the command prompt window open

## How It Works

Reindeer - Python Virtual Environment Manager leverages the ultra-fast [uv](https://github.com/astral-sh/uv) tool to create virtual environments and manage packages, achieving rapid project startup through a series of environment configuration commands. The generated batch files allow consistent activation of environments and execution of scripts.

All operations are performed within the predefined Python environment, ensuring the correct Python version and dependencies are used.

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
