# Wbudowane fikstury pytest - capsys
import sys


def print_user_info(name, age):
    """Function that prints to stdout - we want to test this output"""
    print(f"User: {name}")
    print(f"Age: {age}")
    print("Registration complete!")


def test_capsys_captures_stdout(capsys):
    """Test capsys fixture - captures stdout/stderr for testing"""

    print_user_info("John", 25)

    captured = capsys.readouterr()

    assert "User: John" in captured.out
    assert "Age: 25" in captured.out
    assert "Registration complete!" in captured.out

    assert captured.err == ""


def test_capsys_multiple_captures(capsys):
    """Test multiple capsys captures in single test"""

    print("First output")
    first = capsys.readouterr()
    assert first.out == "First output\n"

    print("Second output")
    second = capsys.readouterr()
    assert second.out == "Second output\n"

    assert first.out != second.out


def test_capsys_with_stderr(capsys):
    """Test capsys capturing both stdout and stderr"""
    print("Normal output")
    print("Error message", file=sys.stderr)

    captured = capsys.readouterr()
    assert captured.out == "Normal output\n"
    assert captured.err == "Error message\n"
