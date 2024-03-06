#!/bin/bash

set -euo pipefail

if [ -z "${POSTGRES_USER}" ]; then
  export POSTGRES_USER="postgres"
fi

export DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"

python << END
import sys
import time
import psycopg2
suggest_unrecoverable_after = 30
start = time.time()
while True:
  try:
    psycopg2.connect(
      dbname="${POSTGRES_DB}",
      user="${POSTGRES_USER}",
      password="${POSTGRES_PASSWORD}",
      host="${POSTGRES_HOST}",
      port="${POSTGRES_PORT}",
    )
    break
  except psycopg2.OperationalError as error:
    sys.stderr.write("Loading PostgreSQL...")
    if time.time() - start > suggest_unrecoverable_after:
      sys.stderr.write(f"This is taking too long. Possibility of an unrecoverable error: '{error}'\n")
  time.sleep(1)
END

>&2 echo "PostgreSQL is available"

exec "$@"
