#!/bin/env bash

set -eu

python -m robot -L "INFO" -P . --outputdir "reports/" "$@" tests/
