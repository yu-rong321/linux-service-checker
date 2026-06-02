from service_checker.checks import check_disk_usage, check_http_url


def test_check_http_url_rejects_invalid_url():
    result = check_http_url("localhost:8000")

    assert result.name == "http_endpoint"
    assert result.healthy is False
    assert "error" in result.details


def test_check_disk_usage_returns_result():
    result = check_disk_usage("/")

    assert result.name == "disk_usage"
    assert "used_percent" in result.details
    assert "free_gb" in result.details
    assert isinstance(result.healthy, bool)