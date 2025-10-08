#!/bin/bash
# last update: 2025-08-30
# https://github.com/hannob/codingstyle
set -euo pipefail

PYLINTIG="consider-using-with,design,fixme,invalid-name,missing-docstring,modified-iterating-list,no-member,possibly-used-before-assignment,protected-access,too-many-lines,unused-argument,broad-exception-caught,c-extension-no-member,duplicate-code,global-statement,global-variable-not-assigned,import-error,import-outside-toplevel,inconsistent-return-statements,redefined-outer-name,unspecified-encoding"
RUFFIG="ANN,C90,D,FIX001,FIX002,ICN001,PLR0911,PLR0912,PLR0913,PLR0915,PTH,S314,S501,S603,SLF001,T201,TD002,TD003,B008,BLE001,COM812,FBT002,I001,N802,N806,PERF203,PERF401,PLC0415,PLR2004,PLW0602,PLW0603,PT009,RET505,RUF100,S202,S310,S607,S608,SIM102,SIM105,SIM108,SIM113,SIM114,SIM115,TD001,TD004,TRY300"

pyfind=$(find -name \*.py)
pygrep=$(grep -rl --exclude-dir=.ruff_cache '^#!/usr/bin/python\|^#!/usr/bin/env python' . || true)
pyfiles=$(echo "$pyfind" "$pygrep" | sort -u)

pycodestyle --max-line-length=100 --ignore=W503,E203 $pyfiles
pyupgrade --py313-plus $pyfiles
pyflakes $pyfiles
flake8 --select=DUO --ignore=DUO107,DUO123,DUO131 $pyfiles
isort --line-length=100 --diff --check-only .
pylint --disable=$PYLINTIG $pyfiles
ruff check --line-length=100 --select=ALL --ignore=$RUFFIG $pyfiles

if [ -d tests ]; then
	python -m unittest -v
fi
