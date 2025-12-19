# Wbudowane fikstury pytest: request
import os


def test_request_fixture(request):
    """Test request fixture - provides test metadata and cleanup functions"""

    # request.node - informacje o teście
    print(f"Test: {request.node.name}")

    # request.addfinalizer - cleanup
    temp_file = "test_temp.txt"
    open(temp_file, "w").write("data")
    # request.addfinalizer - cleanup
    request.addfinalizer(lambda: os.remove(temp_file))

    assert os.path.exists(temp_file)
