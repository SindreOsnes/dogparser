from setuptools import setup, find_packages
import os

VERSION = '0.0.1'
DESCRIPTION = 'Parse dogs from DataEase database files'
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf8') as f: 
    LONG_DESCRIPTION = f.read()

setup(
    name='dogparser',
    version=VERSION,
    author='Sindre Osnes',
    author_email='sindreosnes.git@gmail.com',
    url="https://github.com/SindreOsnes/dogparser",
    license= 'MIT',
    packages=find_packages(exclude=['test']),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    entry_points={
        'console_scripts': [
            'dog=dogparser.runners:parse'
        ]
    },
    install_requires=[
    ],
    test_suite='test',
    python_requires='>=3.7',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Data Parsing',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Python versions
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ]
)