#!/usr/bin/env bash
#./scripts/uninstall.sh
#./scripts/install.sh
./scripts/clean_up.sh
sphinx-apidoc src/faker_file --full -o docs -H 'faker-file' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -f -d 20
cp docs/conf.py.distrib docs/conf.py
cp docs/index.rst.distrib docs/index.rst
