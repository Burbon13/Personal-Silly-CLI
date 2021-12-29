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
        silly=src.my_scripts.silly:cli
        news=src.my_scripts.news:cli
        comm=src.my_scripts.communication:cli
        sysinfo=src.my_scripts.sysinfo:cli
        pdf=src.my_scripts.pdf:cli
        crypto=src.my_scripts.crypto:cli
    ''',
)
