#!/bin/bash

set -euo pipefail

python manage.py migrate --no-input
python manage.py collectstatic --no-input
exec python manage.py runserver 0.0.0.0:8000
