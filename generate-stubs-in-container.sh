#!/bin/bash

set -euo pipefail

if [ ! -f /airflow-scheduler-autorestart ] || [ ! -f /clean-logs ]; then
    echo "This script should only run inside the Airflow container."
    exit 1
fi


AIRFLOW_VERSION="$(airflow version)"
AIRFLOW_INST="$(dirname $(python -c 'import airflow; print(airflow.__file__)'))"

pip install mypy apache-airflow==$AIRFLOW_VERSION apache-airflow-providers-docker

cd /home/airflow
stubgen --inspect-mode --ignore-errors -p airflow -p airflow.providers.docker

cd "$AIRFLOW_INST"

# Find all .pyi files and copy them to the /home/airflow/out/airflow tree
find . -name '*.pyi' -exec cp --parents {} /home/airflow/out/airflow \;
