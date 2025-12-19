# pytest-mock (wrapper na bibliotekę mock, obecnie unittest.mock)
# pip install pytest-mock

from main import len_joke

def test_len_joke(mocker):
    get_joke_mock = mocker.MagicMock()

    res = len_joke(get_joke_mock)
    assert res == 0
