#!/bin/bash
gcloud emulators spanner start &
while ! nc -z localhost 9010; do
  sleep 0.5 # Waiting for Spanner startup.
done
python3 init_db.py
python3 app.py
