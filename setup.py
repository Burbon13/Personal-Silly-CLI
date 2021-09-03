from setuptools import setup, find_packages

setup(
    name='my_silly_cli_tool',
    version='0.1',
    author='Razvan Roatis',
    packages=find_packages(),
    include_package_data=True,
    description='A set of pretty silly personal CLI tasks',
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        silly=src.cmd_scripts.silly:cli
        news=src.cmd_scripts.news:cli
        comm=src.cmd_scripts.communication:cli
    ''',
)
