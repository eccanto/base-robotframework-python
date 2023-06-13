#!/bin/env bash

set -eu

python3 -m robot -L "INFO" -P . --outputdir "reports/" "$@" tests/
