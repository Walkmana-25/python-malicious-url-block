#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from glob import glob

from pybind11.setup_helpers import Pybind11Extension, build_ext



with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ["pybind11"]

test_requirements = [ ]

ext_modules = [
    Pybind11Extension(
        "python_malicious_url_block._utils",
        sorted(glob("python_malicious_url_block/_utils/*.cpp")),

    ),
]

setup(
    author="walkmana-25",
    author_email='walkman.a25@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Malicious Url Block check if it is a malicious URL",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='python-malicious-url-block',
    name='python-malicious-url-block',
    packages=find_packages(include=['python_malicious_url_block', 'python_malicious_url_block.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/walkmana-25/python-malicious-url-block',
    version='0.1.1',
    zip_safe=False,
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules
)
