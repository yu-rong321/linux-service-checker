import shutil
import subprocess
from dataclasses import dataclass
from typing import Any

import psutil
import requests


@dataclass
class CheckResult:
    name: str
    healthy: bool
    details: dict[str, Any]


def check_systemd_service(service_name: str) -> CheckResult:
    """
    Check whether a systemd service is active.

    Example:
        check_systemd_service("docker")
    """
    if not service_name.strip():
        return CheckResult(
            name="systemd_service",
            healthy=False,
            details={"error": "service name is empty"},
        )

    systemctl_path = shutil.which("systemctl")
    if systemctl_path is None:
        return CheckResult(
            name="systemd_service",
            healthy=False,
            details={
                "service": service_name,
                "error": "systemctl not found. This check requires a systemd-based Linux environment.",
            },
        )

    try:
        result = subprocess.run(
            [systemctl_path, "is-active", service_name],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )

        status = result.stdout.strip()

        return CheckResult(
            name="systemd_service",
            healthy=status == "active",
            details={
                "service": service_name,
                "status": status,
                "return_code": result.returncode,
            },
        )

    except subprocess.TimeoutExpired:
        return CheckResult(
            name="systemd_service",
            healthy=False,
            details={
                "service": service_name,
                "error": "systemctl command timed out",
            },
        )


def check_http_url(url: str, timeout: float = 5.0) -> CheckResult:
    """
    Check whether an HTTP endpoint is reachable and returns 2xx/3xx.
    """
    if not url.startswith(("http://", "https://")):
        return CheckResult(
            name="http_endpoint",
            healthy=False,
            details={
                "url": url,
                "error": "URL must start with http:// or https://",
            },
        )

    try:
        response = requests.get(url, timeout=timeout)
        healthy = 200 <= response.status_code < 400

        return CheckResult(
            name="http_endpoint",
            healthy=healthy,
            details={
                "url": url,
                "status_code": response.status_code,
                "response_time_seconds": response.elapsed.total_seconds(),
            },
        )

    except requests.RequestException as exc:
        return CheckResult(
            name="http_endpoint",
            healthy=False,
            details={
                "url": url,
                "error": str(exc),
            },
        )


def check_disk_usage(path: str = "/", warning_threshold: float = 80.0) -> CheckResult:
    """
    Check disk usage percentage.
    """
    usage = psutil.disk_usage(path)
    healthy = usage.percent < warning_threshold

    return CheckResult(
        name="disk_usage",
        healthy=healthy,
        details={
            "path": path,
            "used_percent": usage.percent,
            "warning_threshold": warning_threshold,
            "total_gb": round(usage.total / (1024**3), 2),
            "used_gb": round(usage.used / (1024**3), 2),
            "free_gb": round(usage.free / (1024**3), 2),
        },
    )