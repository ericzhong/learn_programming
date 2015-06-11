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

&nbsp;

    $ cat /usr/lib/python2.7/site-packages/easy-install.pth
    import sys; sys.__plen = len(sys.path)
    ./demo-0.1.0-py2.7.egg
    import sys; new=sys.path[sys.__plen:]; del sys.path[sys.__plen:]; p=getattr(sys,'__egginsert',0); sys.path[p:p]=new; sys.__egginsert = p+len(new)

# Uninstall

1. remove dir
2. delete line in easy-install.pth
