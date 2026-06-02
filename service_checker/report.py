import json
from dataclasses import asdict

from service_checker.checks import CheckResult


def result_to_dict(result: CheckResult) -> dict:
    return asdict(result)


def print_human_report(results: list[CheckResult]) -> None:
    for result in results:
        status = "OK" if result.healthy else "FAIL"

        print(f"[{status}] {result.name}")

        for key, value in result.details.items():
            print(f"  {key}: {value}")

        print()


def print_json_report(results: list[CheckResult]) -> None:
    payload = {
        "overall_healthy": all(result.healthy for result in results),
        "results": [result_to_dict(result) for result in results],
    }

    print(json.dumps(payload, indent=2))