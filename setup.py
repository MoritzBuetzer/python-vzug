"""Set up the Python API for vzug devices."""
import os
import sys
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.rst"), encoding="utf-8") as readme:
    long_description = readme.read()

if sys.argv[-1] == "publish":
    os.system("python3 setup.py sdist upload")
    sys.exit()

setup(
    name="python-vzug",
    version="0.1.1",
    description="Python API for V-ZUG devices",
    long_description=long_description,
    url="https://github.com/MoritzBuetzer/python-vzug",
    author="Moritz Bützer",
    author_email="moritz@buetzer.bz",
    license="Apache License 2.0",
    install_requires=["requests"],
    packages=find_packages(),
    zip_safe=True,
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
)