import os
import re
import codecs
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='PySideX',
    version=find_version("src", "PySideX", "__init__.py"),
    packages=['PySideX'],
    package_dir = {'': 'src'},
    url='',
    license='Apache Software License',
    author='Hugh Sorby',
    author_email='h.sorby@auckland.ac.nz',
    description='Simple wrapper to assist upgrading to PySide2'
)
