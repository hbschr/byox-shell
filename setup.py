from setuptools import setup, find_packages
from byoxshell import __version__

setup(
    name='byoxshell',
    version=__version__,
    author='Heiko Hübscher',
    author_email='heiko.huebscher@gmail.com',
    description='a simple unix shell, following "build your own x"',
    packages=find_packages(),
    extras_require={
        'dev': [
            'flake8>=3.8.4',
            'tox>=3.23.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'byoxshell=byoxshell:main',
        ],
    },
)
