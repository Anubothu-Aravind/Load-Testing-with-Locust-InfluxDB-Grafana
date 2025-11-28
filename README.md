<picture align="center">
  <source media="(prefers-color-scheme: dark)" srcset="https://locust.io/static/img/locust-logo.svg">
  <img alt="Locust + InfluxDB + Grafana" src="https://locust.io/static/img/locust-logo.svg">
</picture>

-----------------

# Load Testing with Locust, InfluxDB & Grafana

| | |
| --- | --- |
| Testing | ![CI - Test](https://img.shields.io/badge/CI%20-%20Test-00BF63)|
| Platform | ![Locust](https://img.shields.io/badge/Locust-1.0+-00BF63?logo=locust)&nbsp;![InfluxDB](https://img.shields.io/badge/InfluxDB-2.x-11A0DB?logo=influxdb)&nbsp;![Grafana](https://img.shields.io/badge/Grafana-8+-F46800?logo=grafana) |
| Meta | [![License - MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE) |

## What is this repository?

This repository provides a reproducible example and tooling to perform distributed load
testing using Locust, to collect time-series metrics in InfluxDB, and to visualize results
with Grafana. It includes example Locust test scenarios, Docker/Docker Compose setups for a
local environment, example InfluxDB write configurations, and ready-to-import Grafana dashboards.

This README is modeled after a structured project overview to help you get started quickly
and understand the pieces included.

## Table of Contents

- [Main Features](#main-features)
- [Where to get it](#where-to-get-it)
- [Dependencies](#dependencies)
- [Quickstart (Docker Compose)](#quickstart-docker-compose)
- [Running Locust Locally (Python)](#running-locust-locally-python)
- [Configuration & Examples](#configuration--examples)
- [License](#license)
- [Documentation](#documentation)
- [Background](#background)
- [Getting Help](#getting-help)
- [Discussion and Development](#discussion-and-development)
- [Contributing](#contributing)

## Main Features

This project provides:

- Example Locust load tests (Python) with realistic user flows and parameterization.
- Metrics exporter configuration to write Locust statistics to InfluxDB.
- Docker Compose to run Locust master/worker, InfluxDB, and Grafana locally.
- Prebuilt Grafana dashboard JSON files for immediate visualization of requests, failures, and resource usage.
- Scripts and make targets to simplify common tasks (start, stop, load, reset-influx).
- Guidance for scaling tests (multiple workers, CI integration, and headless runs).

## Where to get it

The source code is hosted on GitHub:

https://github.com/Anubothu-Aravind/Load-Testing-with-Locust-InfluxDB-Grafana

Clone the repository:

```sh
git clone https://github.com/Anubothu-Aravind/Load-Testing-with-Locust-InfluxDB-Grafana.git
cd Load-Testing-with-Locust-InfluxDB-Grafana
```

## Dependencies

- Docker & Docker Compose (recommended for reproducible local environment)
- Python 3.8+ (for running Locust locally)
- Locust (>= 2.0)
- InfluxDB (v1.x or v2.x  -  configuration examples for both included)
- Grafana (>= 7.x  -  dashboard JSONs included)
- Optional: make, jq, and curl for convenience scripts

See the individual configuration files (docker-compose.yml, requirements.txt) for exact versions.

## Quickstart (Docker Compose)

Start the full stack (Locust master + 2 workers, InfluxDB, Grafana):

```sh
docker compose up -d
```

- Open Locust web UI: http://localhost:8089
- Open Grafana: http://localhost:3000
  - Default Grafana credentials: admin/admin (change on first login)
- Import the dashboard JSON files from dashboards/ into Grafana or add the supplied provisioning

Stop and remove containers:

```sh
docker compose down
```

Reset InfluxDB data (example script included):

```sh
./scripts/reset_influx.sh
```

## Running Locust Locally (Python)

Create virtual environment and install requirements:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run Locust in headless mode (example):

```sh
locust -f locustfile.py --headless -u 100 -r 10 --run-time 5m --host https://target.example.com
```

To send metrics to InfluxDB, configure the environment variables or modify locustfile.py to point to your InfluxDB endpoint.

## Configuration & Examples

- locustfile.py  -  example user behavior and tasks
- docker-compose.yml  -  orchestrates Locust, InfluxDB, Grafana
- influx/  -  sample InfluxDB configuration and initialization scripts
- grafana/dashboards/  -  Grafana dashboard JSON to import or provision
- scripts/  -  helper scripts for common operations (reset, provision, run headless)

Tips:
- Tune worker count and hatch rate (--workers, -u, -r) for target traffic.
- Use Grafana dashboards to inspect latency distributions, failure rates, and request throughput.
- Persist InfluxDB data by configuring volumes in docker-compose.yml for long-term analysis.

## License

This project is available under the MIT License. See the LICENSE file for details.

## Documentation

Detailed usage notes, configuration examples, and dashboard descriptions are in the docs/ folder (if present). For quick reference:

- Locust docs: https://locust.io
- InfluxDB docs: https://docs.influxdata.com
- Grafana docs: https://grafana.com/docs

## Background

This repository was created to provide a simple, reproducible setup for teams to
get started with load testing web services and to collect and visualize performance
metrics in a time-series database. It aims to reduce the initial friction of wiring
together Locust, InfluxDB, and Grafana so you can focus on designing meaningful tests.

## Getting Help

If you run into issues or need assistance:

- Open an issue on this repository: https://github.com/Anubothu-Aravind/Load-Testing-with-Locust-InfluxDB-Grafana/issues
- Include reproduction steps, logs, and configuration snippets (docker-compose.yml, locustfile.py)
- For general Locust/InfluxDB/Grafana questions, consult the official docs linked above or community forums.

## Discussion and Development

Development happens on GitHub. Use the issue tracker for bug reports and feature requests.
If you intend to add dashboards or helper scripts, please follow the contribution guidelines.

## Contributing

All contributions are welcome  -  bug reports, fixes, documentation improvements, and new example scenarios.

Please follow these steps to contribute:

1. Fork the repository and create a feature branch: git checkout -b feat/my-change
2. Run tests and linters (if included)
3. Open a Pull Request with a clear description of the change
4. Follow the repository's Code of Conduct (if present) and be respectful in discussions

<hr>

[Go to Top](#table-of-contents)
