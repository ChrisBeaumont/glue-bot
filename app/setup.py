"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Glue.py']
DATA_FILES = [
]

OPTIONS = {
    'argv_emulation': False,
    'packages': ['zmq', 'glue', 'pyfits', 'pywcs', 'matplotlib', 'pygments', 'vo', 'atpy', 'aplpy', 'scipy', 'numpy', 'IPython'],
    'includes': ['PyQt4', 'PyQt4.QtCore', 'PyQt4.QtGui', 'sip'],
    'excludes': ['PyQt4.QtDesigner', 'PyQt4.QtNetwork', 'PyQt4.QtNetwork', 'PyQt4.QtOpenGL', 
        'PyQt4.QtScript', 'PyQt4.QtSql', 'PyQt4.QtTest', 'PyQt4.QtWebKit', 'PyQt4.QtXml', 
        'PyQt4.phonon', 'Tkinter'],
    }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)    

