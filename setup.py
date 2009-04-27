from setuptools import setup, find_packages

install_requires = []

classifiers = """
Intended Audience :: Education
Intended Audience :: Developers
Intended Audience :: Information Technology
License :: OSI Approved :: GNU General Public License (GPL)
Programming Language :: Python
Development Status :: 3 - Alpha
"""

setup(
    name = 'brooklynmuseumapi',
    version = '0.1.0',  # update brooklynmuseumapi/__init__.py on release!
    url = 'http://bitbucket.org/anarchivist/brooklynmuseumapi',
    author = 'Mark A. Matienzo',
    author_email = 'mark@matienzo.org',
    license = 'GPL',
    packages = find_packages(),
    install_requires = install_requires,
    description = 'Interact with the Brooklyn Museum Collection API',
    classifiers = filter(None, classifiers.split('\n')),
)
