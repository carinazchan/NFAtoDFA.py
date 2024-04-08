import pytest
import sys
import ReadWrite
from unittest.mock import Mock


@pytest.fixture
# Fixture that creates a mock object to represent command-line arguments.
def mock_args(monkeypatch):
    args = Mock()
    monkeypatch.setattr("sys.argv", ["test.py", "--arg1", "value1", "--arg2", "value2"])
    return args


def test_command_line_args(mock_args):
    assert mock_args.arg1 == "value1"
    assert mock_args.arg2 == "value2"


def test___init__(mock_args):
    # Create an instance of ReadWrite.
    ReadWrite_instance = ReadWrite.ReadWrite()

    # Check if the inputFilePath is taken from the command line arguments.
    assert ReadWrite_instance.inputFilePath == mock_args.argv[1]


# def test_WriteToOutput():
#     # Setup.
#     inputFilePath = "input.nfa"
#     outputFilePath = "output.dfa"

#     # Create an instance of ReadWrite.
#     ReadWrite_instance = ReadWrite(inputFilePath, outputFilePath)

#     # Call the method to be tested.
#     ReadWrite_instance.WriteToOutput(outputFilePath)
