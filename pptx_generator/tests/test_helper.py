import pytest
from pptx_generator.helper import validate_and_execute


def test_validate_and_execute(capsys):
    # Test case: Valid input with .json extension
    user_input = {"json": "sample.json"}
    validate_and_execute(user_input)
    captured = capsys.readouterr()
    assert "please enter only the filenames with their extensions" not in captured.out

    # Test case: Invalid input with invalid extension
    user_input = {"json": "data.txt"}
    validate_and_execute(user_input)
    captured = capsys.readouterr()
    assert "please enter only the filenames with their extensions" in captured.out

    # Test case: Invalid input with no extension
    user_input = {"json": "sample"}
    validate_and_execute(user_input)
    captured = capsys.readouterr()
    assert "please enter only the filenames with their extensions" in captured.out

    # Test case: Invalid input with an empty dictionary
    user_input = {}
    validate_and_execute(user_input)
    captured = capsys.readouterr()
    assert "please enter one file name!" in captured.out


if __name__ == '__main__':
    pytest.main()