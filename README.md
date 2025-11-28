# Opptym Locust Toolkit

This toolkit consolidates multiple Locust test scenarios, a docker-compose stack (Locust master/workers + InfluxDB + Grafana), and a sample Grafana dashboard for visualizing test metrics. Use this in staging only.

## Quickstart (local)

1. Install prerequisites: `docker` and `docker-compose` (or `docker compose`).
2. Start stack: `docker compose up -d` (this launches InfluxDB and Grafana)
3. From the repo root, run a quick smoke test:
   ```bash
   ./run-tests.sh basic 10 5
   ```

## What each mode does
- `basic` — simple homepage + health checks
- `step` — progressive step ramp
- `rps` — constant pacing / throughput-focused
- `api_mixed` — simulated authenticated read/write API workload
- `db_heavy` — DB-heavy endpoints (staging only)

## Safety checklist
- Always target staging (`--host=https://staging.opptym.com`) unless you have written permission.
- Start with small user counts (10–30) and increase slowly.
- Notify hosting/CDN providers if you plan large tests.
- Use test accounts and idempotent endpoints.

## Monitoring
Grafana is available at `http://localhost:3000` (default admin/admin) after running `docker compose up`. Import `grafana-dashboard.json`.


## Added in follow-up
- Improved Grafana dashboard for Influx: grafana-dashboard-improved.json
- Prometheus + Grafana example: docker-compose-prometheus.yml and prometheus.yml
- Prometheus-targeted Grafana dashboard: grafana-dashboard-prometheus.json
- RUNBOOK.md — interpreting results and prioritized fixes
