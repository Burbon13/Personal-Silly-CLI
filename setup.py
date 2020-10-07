from setuptools import setup

setup(
    name='my_funny_script',
    version='0.1',
    py_modules=['terminal'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        silly=src.cmd_scripts.silly:cli
    ''',
)
