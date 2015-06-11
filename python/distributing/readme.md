# Install

    python setup.py bdist_egg
    sudo python setup.py install

# Test

    >>> from demo import test
    >>> test.test()
    Hello, egg demo!

# Files

    /usr/lib/python2.7/site-packages/demo-0.1.0-py2.7.egg/
    ├── demo
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── test.py
    │   └── test.pyc
    └── EGG-INFO
        ├── dependency_links.txt
        ├── not-zip-safe
        ├── PKG-INFO
        ├── SOURCES.txt
        └── top_level.txt
    
    2 directories, 9 files
