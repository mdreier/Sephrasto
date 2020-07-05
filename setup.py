"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Sephrasto.py']
DATA_FILES = ['datenbank.xml', 'Charakterbogen.pdf', 'Charakterbogen_lang.pdf']
OPTIONS = {'iconfile': 'icon_large.icns', 'includes': ['PyQt5']}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)