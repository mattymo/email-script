from setuptools import setup
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='email-script',
    version='1.0.0',
    description='Sends notification message about running aws instances to the specified recipient every week (by default).',
    url='https://github.com/tikitavi/email-script',
    author='Anastasia Kravets',
    author_email='rtikitavi@gmail.com', 
    keywords='email, aws',
    packages=['emailscript'],
)