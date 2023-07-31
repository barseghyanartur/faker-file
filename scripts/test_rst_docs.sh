#!/usr/bin/env bash
#find . -name "*.rst" | xargs pytest
pytest *.rst docs/*.rst
