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

# Deactivate the env (execute when you finished with the "run" part)
deactivate
```

# Run

```shell
#  Install a project in editable mode (i.e. setuptools "develop mode") from the local project path
pip install -e .

# Set the environment variables
. ./setup_env_vars.sh   # Or setup_env_vars.bat for Windows

# Now feel free to execute any command
# Commands available. Run with --help to see what options you have.
silly 
news
comm
```

# Util links

[Python venv](https://docs.python.org/3/library/venv.html)

[Setuptools documentation](https://setuptools.readthedocs.io/en/latest/)

[Click documentation](https://click.palletsprojects.com)

[Setuptools integration with Click](https://click.palletsprojects.com/en/8.0.x/setuptools/)

# Troubleshooting

[Module src not found issue](https://stackoverflow.com/questions/49838927/click-module-setuptools-example-didnt-work-out-of-the-box)
