# pytest-mock (wrapper na bibliotekę mock, obecnie unittest.mock)
# pip install pytest-mock

from main import get_joke

def test_get_joke(mocker):
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "value": "A super joke"
    }

    with mocker.patch("main.requests") as mock_requests:
        mock_requests.get.return_value = mock_response
        res = get_joke()

    assert res == "A super joke"


# def test_fail_get_joke(monkeypatch):
#     mock_requests = MagicMock()
#     mock_response = MagicMock(status_code=300)
#     mock_requests.get.return_value = mock_response
#
#     monkeypatch.setattr("main.requests", mock_requests)
