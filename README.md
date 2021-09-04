# About

A collection of random CLI commands which I though would be nice/fun to implement and have.

# Install

## Prerequisites

- Python 3
- pip

## Steps

```shell
# Create the virtual environment
python3 -m venv env

# Activate the env
source env/bin/activate

# Deactivate the env
deactivate

```

# Run

```shell
# Build the commands
pip install -e .

# Set the environment variables
. ./setup_env_vars.sh   # Or setup_env_vars.bat for Windows

# Now feel free to execute any command

# Commands available. Run with --help to see what options you have.
silly 
news
comm
```
