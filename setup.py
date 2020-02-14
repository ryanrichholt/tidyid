from setuptools import setup, find_packages
from os import path

scriptdir = path.abspath(path.dirname(__file__))
readme = path.join(scriptdir, 'README.md')

with open(readme, encoding='utf-8') as fp:
    long_description = fp.read()


setup(
    name='tidyid',
    version='1.0', 
    description='Sample identifiers that are easy to read and write', 
    long_description=long_description,
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/ryanrichholt/tidyid', 
    author='Ryan Richholt',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='sample bioinformatics identifiers', 
    python_requires='>=3.6',
    py_modules=['tidyid'],
    entry_points={
        'console_scripts': [
            'tidyid=tidyid:main',
        ],
    }
)
