# monkeypatching fixture

from unittest.mock import MagicMock

from main import get_joke


def test_get_joke(monkeypatch):
    mock_requests = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "value": "A super joke"
    }
    mock_requests.get.return_value = mock_response

    monkeypatch.setattr("main.requests", mock_requests)

    assert get_joke() == "A super joke"

def test_fail_get_joke(monkeypatch):
    mock_requests = MagicMock()
    mock_response = MagicMock(status_code=300)
    mock_requests.get.return_value = mock_response

    monkeypatch.setattr("main.requests", mock_requests)

    assert get_joke() == ""
