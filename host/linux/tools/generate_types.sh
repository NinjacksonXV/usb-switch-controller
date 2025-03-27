#!/usr/bin/env bash
curl -s https://raw.githubusercontent.com/pygobject/pygobject-stubs/refs/heads/master/tools/parse.py > ./parse.py
curl -s https://raw.githubusercontent.com/pygobject/pygobject-stubs/refs/heads/master/tools/generate.py > ./generate.py
python ./generate.py UDisks 2.0 > ../typings/gi-stubs/repository/UDisks.pyi
