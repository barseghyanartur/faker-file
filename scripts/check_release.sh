#!/usr/bin/env bash
#python setup.py register
python setup.py sdist bdist_wheel
twine check dist/* --verbose
