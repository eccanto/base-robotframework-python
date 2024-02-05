#!/usr/bin/env bash

set -xeu

VENV_NAME=".venv"

python -m venv --system-site-packages "${VENV_NAME}"

# shellcheck disable=SC1091
source "${VENV_NAME}"/bin/activate

ln -s /usr/lib/python3/dist-packages/pyatspi* "$VIRTUAL_ENV"/lib/python*/site-packages
pip install -r requirements.txt
