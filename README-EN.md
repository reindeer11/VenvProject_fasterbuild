# Reindeer - Python Virtual Environment Manager

[中文](README.md)

Reindeer is a graphical tool designed to simplify the setup and management of Python projects. With a clean and beautiful interface, it makes it easy to create virtual environments, manage dependencies, and execute scripts.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey.svg)

## Features

- Create Python virtual environments using the ultra-fast `uv` tool
- Automatically install dependencies from `requirements.txt`
- Generate Windows batch files for quick project startup
- Configurable custom package index mirror sources
- Execute Python scripts within virtual environments
- Beautiful, modern colored graphical interface

## Requirements

- Python 3.7+
- [uv](https://github.com/astral-sh/uv) - An extremely fast Python package installer and resolver
- Predefined Python environment located at: `G:\cpr\project_to_github\Portable_configuration_environment\Scripts\activate.bat`

## Installation

1. Ensure the predefined environment exists (configured at `G:\cpr\project_to_github\Portable_configuration_environment`)
2. Clone or download this repository
3. Install required dependencies (if not already present in the environment):
   ```
   pip install -r requirements.txt
   ```
4. Install uv (if not already present in the environment):
   ```
   pip install uv
   ```

## Usage

To start the application:

1. Manually activate the predefined environment:

   ```
   G:\cpr\project_to_github\Portable_configuration_environment\Scripts\activate.bat
   ```

2. Run the application:
   ```
   python run.py
   ```

## Packaging

This project can be packaged into an executable file using PyInstaller.

### Packaging Process

1. Install PyInstaller:

   ```
   pip install pyinstaller
   ```

2. Create executable file using the spec file:
   ```
   pyinstaller Reindeer.spec
   ```

This will generate a standalone executable in the `dist` folder.

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

Reindeer leverages the ultra-fast [uv](https://github.com/astral-sh/uv) tool to create virtual environments and manage packages. The generated batch files allow consistent activation of environments and execution of scripts.

All operations are performed within the predefined Python environment, ensuring the correct Python version and dependencies are used.

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
