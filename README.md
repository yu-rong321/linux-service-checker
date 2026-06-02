
````markdown
# Linux Service Checker

A Python-based CLI tool for checking Ubuntu/Linux service health.

## Overview

Linux Service Checker is a lightweight command-line tool for basic service and system health diagnostics in Ubuntu/Linux environments.

It currently supports:

- Disk usage checks
- HTTP endpoint health checks
- systemd service status checks
- Human-readable output
- JSON output for automation
- Automated tests with pytest
- GitHub Actions CI on Ubuntu runners

## Features

### Disk Usage Check

```bash
service-checker --disk
````

### HTTP Endpoint Check

```bash
service-checker --url https://example.com
```

### systemd Service Check

```bash
service-checker --service docker
```

This feature requires a systemd-based Linux environment such as Ubuntu or WSL Ubuntu.

### JSON Output

```bash
service-checker --disk --json
```

## Installation

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -e .
```

### Ubuntu / Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage

Run a disk check:

```bash
service-checker --disk
```

Run an HTTP endpoint check:

```bash
service-checker --url https://example.com
```

Run a systemd service check:

```bash
service-checker --service docker
```

Run multiple checks with JSON output:

```bash
service-checker --disk --url https://example.com --json
```

## Testing

```bash
pytest
```

## Technical Focus

This project demonstrates:

* Python CLI development
* Linux service diagnostics
* HTTP health check validation
* JSON reporting
* pytest-based automated testing
* GitHub Actions CI on Ubuntu runners

## Roadmap

* Port checking
* CPU and memory checks
* Docker container health checks
* Markdown report export
* Debian package support for Ubuntu installation

````
