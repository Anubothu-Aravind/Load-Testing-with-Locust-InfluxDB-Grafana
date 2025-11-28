#!/usr/bin/env bash
set -e

MODE=${1:-basic}
USERS=${2:-50}
SPAWN_RATE=${3:-5}
HOST=${4:-https://staging.opptym.com}

case "$MODE" in
  basic)
    FILE=locustfiles/locustfile_basic.py
    ;;
  step)
    FILE=locustfiles/locustfile_step.py
    ;;
  rps)
    FILE=locustfiles/locustfile_rps.py
    ;;
  api_mixed)
    FILE=locustfiles/locustfile_api_mixed.py
    ;;
  db_heavy)
    FILE=locustfiles/locustfile_db_heavy.py
    ;;
  *)
    echo "Unknown mode: $MODE"; exit 1
    ;;
esac

echo "Running mode=$MODE file=$FILE users=$USERS spawn_rate=$SPAWN_RATE host=$HOST"
locust -f $FILE --headless -u $USERS -r $SPAWN_RATE --host=$HOST --run-time 5m --csv=results/${MODE}_run || true
