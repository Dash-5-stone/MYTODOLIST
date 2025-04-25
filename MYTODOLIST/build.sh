#!/usr/bin/env bash
set -o errexit  # exit on error

python -m pip install --upgrade pip
pip install poetry==1.7.1
poetry install --no-root; poetry export --without-hashes --format=requirements.txt --output=requirements.txt
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
