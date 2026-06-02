import argparse

from service_checker.checks import (
    check_disk_usage,
    check_http_url,
    check_systemd_service,
)
from service_checker.report import print_human_report, print_json_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="service-checker",
        description="Check Ubuntu/Linux service health from the command line.",
    )

    parser.add_argument(
        "--service",
        help="Check a systemd service, for example: docker, ssh, postgresql",
    )

    parser.add_argument(
        "--url",
        help="Check an HTTP health endpoint, for example: http://localhost:8000/healthz",
    )

    parser.add_argument(
        "--disk",
        action="store_true",
        help="Check disk usage for the root filesystem.",
    )

    parser.add_argument(
        "--disk-path",
        default="/",
        help="Disk path to check. Default: /",
    )

    parser.add_argument(
        "--disk-threshold",
        type=float,
        default=80.0,
        help="Disk warning threshold percentage. Default: 80",
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON.",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    results = []

    if args.service:
        results.append(check_systemd_service(args.service))

    if args.url:
        results.append(check_http_url(args.url))

    if args.disk:
        results.append(
            check_disk_usage(
                path=args.disk_path,
                warning_threshold=args.disk_threshold,
            )
        )

    if not results:
        parser.error("Please provide at least one check: --service, --url, or --disk")

    if args.json:
        print_json_report(results)
    else:
        print_human_report(results)


if __name__ == "__main__":
    main()