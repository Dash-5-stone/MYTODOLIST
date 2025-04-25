#!/usr/bin/env bash
set -o errexit  # exit on error

python -m pip install --upgrade pip
pip install poetry==1.7.1
poetry export --without-hashes -f requirements.txt -o requirements.txt
pip install -r requirements.txt

python manage.py collectstatic --no-input

