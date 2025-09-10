"""
SQLAlchemy Learning Project Setup Script

This script provides an easy way to set up the SQLAlchemy learning environment
and install all necessary dependencies for the tutorial series.

Usage:
    python setup.py install
    python setup.py develop
    python setup.py test
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements from requirements.txt
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="sqlalchemy-learn",
    version="1.0.0",
    author="SQLAlchemy Learning Project",
    author_email="your-email@example.com",
    description="A comprehensive SQLAlchemy tutorial series with practical examples",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/SQLA-Learn",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Database",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "isort>=5.12.0",
        ],
        "docs": [
            "sphinx>=6.0.0",
            "sphinx-rtd-theme>=1.2.0",
        ],
        "jupyter": [
            "jupyter>=1.0.0",
            "ipykernel>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "sqlalchemy-learn=NeuralNine.main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="sqlalchemy, database, orm, tutorial, learning, python",
    project_urls={
        "Bug Reports": "https://github.com/your-username/SQLA-Learn/issues",
        "Source": "https://github.com/your-username/SQLA-Learn",
        "Documentation": "https://github.com/your-username/SQLA-Learn#readme",
    },
)
