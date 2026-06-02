A Python-based CLI tool for checking Ubuntu/Linux service health.

## Overview

Linux Service Checker is a lightweight command-line tool designed to verify basic service and system health in Ubuntu/Linux environments.

It currently supports:

- Disk usage checks
- HTTP endpoint health checks
- systemd service status checks
- Human-readable output
- JSON output for automation and CI/CD integration
- Automated tests with pytest

## Features

### Disk Usage Check

Check whether disk usage is below a warning threshold.

```bash
service-checker --disk

Example output:

[OK] disk_usage
  path: /
  used_percent: 46.6
  warning_threshold: 80.0
  total_gb: 346.67
  used_gb: 161.61
  free_gb: 185.07
HTTP Endpoint Check

Check whether an HTTP endpoint returns a successful status code.

service-checker --url https://example.com
systemd Service Check

Check whether a Linux systemd service is active.

service-checker --service docker

Note: this feature requires a systemd-based Linux environment such as Ubuntu or WSL Ubuntu.

JSON Output

Generate structured JSON output for automation.

service-checker --disk --json

Example output:

{
  "overall_healthy": true,
  "results": [
    {
      "name": "disk_usage",
      "healthy": true,
      "details": {
        "path": "/",
        "used_percent": 46.6,
        "warning_threshold": 80.0,
        "total_gb": 346.67,
        "used_gb": 161.61,
        "free_gb": 185.07
      }
    }
  ]
}
Installation

Create and activate a virtual environment.

Windows PowerShell
python -m venv .venv
.venv\Scripts\activate
pip install -e .
Ubuntu / Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
Usage

Check disk usage:

service-checker --disk

Check an HTTP health endpoint:

service-checker --url https://example.com

Check a systemd service:

service-checker --service docker

Output JSON:

service-checker --disk --json

Run multiple checks:

service-checker --disk --url https://example.com --json
Testing

Run automated tests:

pytest
Project Structure
linux-service-checker/
├── service_checker/
│   ├── __init__.py
│   ├── checks.py
│   ├── cli.py
│   └── report.py
├── tests/
│   └── test_checks.py
├── pyproject.toml
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
Technical Focus

This project demonstrates:

Python CLI development
Linux service diagnostics
HTTP health check validation
JSON reporting
pytest-based automated testing
GitHub Actions CI on Ubuntu runners
Roadmap

Planned improvements:

Port checking
CPU and memory checks
Docker container health checks
Markdown report export
Debian package support for Ubuntu installation