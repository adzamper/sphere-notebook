"""

Build and install the project: geoscilabs

geoscilabs are the codes that support the interactive labs provided through
https://gpg.geosci.xyz and https://em.geosci.xyz
"""

from distutils.core import setup
from setuptools import find_packages

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Education",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Topic :: Scientific/Engineering :: Physics",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Operating System :: MacOS",
    "Natural Language :: English",
]

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="sphereob",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.7",
        "scipy>=1.0",
        "matplotlib>2.1",
        "ipywidgets",
        "SimPEG>=0.14.1",
        "discretize>=0.4.14",
        "empymod>=2.0.0",
        "jupyter",
        "deepdish",
        "Pillow",
        "requests",
        "cvxopt",
        "quadpy",
    ],
    author="spherob",
    author_email="adzamper7117@gmail.com",
    description="EMLAB",
    long_description=LONG_DESCRIPTION,
    keywords="geophysics, electromagnetics",
    classifiers=CLASSIFIERS,
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    license="MIT License",
    use_2to3=False,
)